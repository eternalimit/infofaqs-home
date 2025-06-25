#!/bin/bash

# Sync dev and staging with main
echo "Syncing branches with main..."

for branch in dev staging admin; do
  echo "Merging main into $branch..."
  git checkout $branch
  git merge main
  git push origin $branch
done

echo "✅ Sync complete."
