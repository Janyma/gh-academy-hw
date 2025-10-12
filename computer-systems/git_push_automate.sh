#!/usr/bin/env bash

repo_directory="/Users/zhanylmyrzasanzharbekova/gh-academy-hw/gh-academy-hw-1"
branch="main"
git_message="New changes found via git scrippt  $(date '+%d.%m.%Y
%H%:M:%S')"
cd "$repo_directory" || { echo "Repository nicht gefunden"; exit 1; }

if [ ! -d ".git" ]; then
    echo "Kein Git-Repository hier: $repo_directory"
    exit 1
fi

git fetch origin "$branch" >/dev/null 2>&1

if [ -n "$(git status --porcelain)" ]; then
    echo "Änderungen gefunden"
    git add .
    git commit -m "$git_message"
    git push origin "$branch"
else
    echo "no changes"
fi
