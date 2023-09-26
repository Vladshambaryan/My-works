"""
git clone your_repository_link - clone repository to your local computer
git status
git add .
git add *.py
git add !*.txt
git add !index.txt
git add folder_name/
git add folder_name/*.py
git add !folder_name/*.txt
git rm -r --cached file_name #untrack local file or folder udalenie

git commit -m "message"
git push - Push the branch to your remote main branch repository
git push origin master - Push the branch to your remote master repository
git push origin <your_branchname> - Push the branch to your branch remote repository
git pull - update your local repository

git log
git log --oneline
git checkout commit_id
git checkout master
git checkout your_branch_name
:q - exit from LESS with VIM command

git branch your_branch_name - create your branch
git checkout your_branch_name - go to your branchq
git checkout -b your_branch_name - create your new branch and go to your branch
git branch - shows your local branches
git branch -a - see ALL branches
git branch -d <branchname> - Delete the feature branch
git remote - check repository connection

git revert commit_id - cancel commit
git reset commit_id --hard - delete commit

How to recover deleted Branch from Command line?
1.You have to know your last commit message from your deleted branch.
git reflog
# Search for message in the list
# 10ce202 HEAD@{1}: commit: <last commit message>

# Now you have two options, either checkout revision or HEAD
git checkout 10ce202
# Or
git checkout HEAD@{1}

# Create branch
git branch recovered-branch

# You may want to push that back to remote
git push origin recovered-branch:recovered-branch

"""