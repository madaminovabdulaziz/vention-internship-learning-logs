
First of all, let's set up a mental model on GIT.

SO what is GIT?

Git is a tiny database of snapshots of my project.
Every git command I am doing, it is either creating a snapshot, 
either moving a pointer, or either it is asking database, I mean fetching from database


Hidden ./git folder is that database, if I delete it, it means I deleted the entire repository.


The files that I work on, I mean edit them called: working directory, or working tree



## NOW, let's learn a bit git commands:

### 1. git status -> what's the current situation?
So git status basically returns, or shows:
1. In which branch I am? Where is HEAD is pointing?
2. Files waiting to be commited
3. files that have been modified but not staged
4. Files git has never seen before

# git status -s -> see untracked fikes

# git add -> when I type this command, git takes all files, converts to SHA-1 hashing, and puts to .git/objects folder, 
# and updates staging are pointing at it

NOTE: git add -p: walks through each chunk of changes and asks: stage this?y/n


# git commit -m -> freeze curretn snapshot


# git log --oneline --graph --all --decorate -> see all history logs of commits


git config --global alias.lg "log --oneline --graph --all --decorate" -> does the thing above making "git lg" as alias




git branch -> shows in what branch we are currently in

git branch foo -> creates new branch called foo

git switch foo -> switches to branch foo


git branch -d foo deletes branch 
## NOTE: Deleting branch deletes the pointer not the commits, you can rescue them in ~30 days with git reflog


r-2 day-01-basics % cd git-internals-demo 
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git init
Initialized empty Git repository in /Users/abdulazizmadaminov/Desktop/Vention-Internship/week-03-git-docker/day-01-basics/git-internals-demo/.git/
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % echo "HELLO" > greeting.txt
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git add greeting.txt 
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git commit -m "first commit"
[main (root-commit) 02153c7] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 greeting.txt
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git log --online
fatal: unrecognized argument: --online
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git log --oneline
02153c7 (HEAD -> main) first commit
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git cat-file -t 02153c7
commit
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git cat-file -p 02153c7
tree 0fa09c32c55fddcab382ad348518e5984571ced5
author = <=> 1778050099 +0500
committer = <=> 1778050099 +0500

first commit
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git cat-file -p 0fa09c32c55fddcab382ad348518e5984571ced5
100644 blob e427984d4a2c1904681f2e2ee5980f37640d353f    greeting.txt
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git cat-file -p e427984d4a2c1904681f2e2ee5980f37640d353f
HELLO
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % cat .git/HEAD
ref: refs/heads/main
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % cat .git/refs/heads/main
02153c7c6371912ed46f6576205bc1d8853256af
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % git cat-file -p 02153c7c6371912ed46f6576205bc1d8853256af
tree 0fa09c32c55fddcab382ad348518e5984571ced5
author = <=> 1778050099 +0500
committer = <=> 1778050099 +0500

first commit
(venv) abdulazizmadaminov@Abdulazizs-MacBook-Air-2 git-internals-demo % 