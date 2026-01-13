const {MongoClient, ObjectId, ReturnDocument}=require("mongodb");
const uri="mongodb+srv://123janyl456_db_user:qBWFajtZx2NlNtnM@workoutcluster.8tflspo.mongodb.net/?retryWrites=true&writeConcern=majority";
if(!uri){
    throw new Error("Please define the MONGODB_URI environment variable inside .env.local");
}
const client = new MongoClient(uri);

async function run(fn) {
    await client.connect();
    try {
        const db = client.db("workout");
        const collection = db.collection("workouts");
        return await fn(collection);
    } finally {
        await client.close();
    }
}

const getAllWorkouts = async ()=>{
    return await run(async (collection) => {
        const docs =await collection.find({}).toArray();
        if(docs.length===1 && Array.isArray(docs[0].workouts)){
            return docs[0].workouts;
        }
        return docs;
    });
};

const getOneWorkout = async (workoutId) => {
    return await run(async(collection) => {
        const query = ObjectId.isValid(workoutId) ? {_id: new ObjectId(workoutId)} : {id: workoutId};
        return await collection.findOne(query);
    });
}

const createNewWorkout = async (newWorkout) => { 

   return await run(async (collection) => {
    newWorkout.createdAt = new Date().toLocaleString("en-US", {timeZone: "UTC"});
    newWorkout.updatedAt = new Date().toLocaleString("en-US", {timeZone: "UTC"});

    try{
           const res = await collection.insertOne(newWorkout);
           return await collection.findOne({_id: res.insertedId});
    }catch (error){
        throw {status: 500, message: error?.message || error}
    }


   });

};

const updateOneWorkout =(workoutId, changes) =>{
    return run(async (collection) => {
        const filter = ObjectId.isValid(workoutId) ? {_id: new ObjectId(workoutId)} : {id: workoutId};

        const updateDoc = {
            $set: {
                ...changes,
                updatedAt: new Date().toLocaleString("en-US", {timeZone: "UTC"})
            }
        };
        const res = await collection.findOneAndUpdate(filter, updateDoc, { ReturnDocument: "after"});
        return res.value;
    });
}

const deleteOneWorkout = (workoutId)=>{
    return run(async (collection) => {
        const filter = ObjectId.isValid(workoutId) ? {_id: new ObjectId(workoutId)} : {id: workoutId};
        const res=await collection.deleteOne(filter);
        return res.deletedCount===1;
    });
    // const indexForDeletion =DB.workouts.findIndex(
    //     (workout)=workout.id ===workoutId
    // );

    // if(indexForDeletion===-1){
    //     return
    // }

    // DB.workouts.splice(indexForDeletion, 1);
    // saveToDatabase(DB)
}

module.exports={getAllWorkouts,
    createNewWorkout,
    deleteOneWorkout,
    updateOneWorkout,
    getOneWorkout
}