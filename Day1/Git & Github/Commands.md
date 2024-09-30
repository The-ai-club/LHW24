# Git Commands and Descriptions

## Git Basics

1. **git init**
   - Initializes a new Git repository in your project directory.
   - Example:
     ```bash
     git init
     ```

2. **git add**
   - Adds changes in the working directory to the staging area, preparing them for the next commit.
   - Example:
     ```bash
     git add <file-name>
     ```
   - To add all files:
     ```bash
     git add .
     ```

3. **git commit**
   - Records the changes from the staging area to the repository with a message describing the changes.
   - Example:
     ```bash
     git commit -m "Describe your changes here"
     ```

4. **git status**
   - Shows the state of the working directory and the staging area. It displays which files have been modified, which files are in the staging area, and which are not.
   - Example:
     ```bash
     git status
     ```

5. **git push**
   - Uploads your committed changes to a remote repository, such as GitHub.
   - Example:
     ```bash
     git push origin <branch-name>
     ```

6. **git pull**
   - Fetches changes from a remote repository and merges them into your current branch.
   - Example:
     ```bash
     git pull origin <branch-name>
     ```

---

## Branching & Merging

1. **git branch**
   - Lists all branches in your repository and highlights the current branch.
   - Example:
     ```bash
     git branch
     ```
   - To create a new branch:
     ```bash
     git branch <branch-name>
     ```

2. **git checkout**
   - Switches to a specified branch or commit.
   - Example:
     ```bash
     git checkout <branch-name>
     ```

3. **git merge**
   - Merges the changes from one branch into another.
   - Example:
     ```bash
     git merge <branch-name>
     ```

---

## Collaboration Commands

1. **git clone**
   - Creates a local copy of a remote repository.
   - Example:
     ```bash
     git clone <repository-url>
     ```

2. **git remote**
   - Manages remote connections to your repository. This is used to add or remove a connection to a remote server, such as GitHub.
   - Example (to add a new remote):
     ```bash
     git remote add origin <repository-url>
     ```

3. **git fetch**
   - Downloads commits, files, and refs from a remote repository, but it does not merge them into your current branch.
   - Example:
     ```bash
     git fetch origin
     ```

---

## Undoing Changes

1. **git reset**
   - Resets your staging area and working directory to match the most recent commit.
   - Example (soft reset):
     ```bash
     git reset --soft HEAD~1
     ```

2. **git revert**
   - Creates a new commit that undoes the changes from a previous commit without altering the commit history.
   - Example:
     ```bash
     git revert <commit-hash>
     ```

---

## Additional Resources:
- For more advanced Git commands, visit the [Git Official Documentation](https://git-scm.com/doc).
