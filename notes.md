# Part A – Repository Initialization & Basic Git Commands

## Git

Git is a Distributed Version Control System (DVCS) used to track changes in source code, maintain project history, and enable collaboration among developers.

## Repository

A repository is a storage location that contains the project files along with Git history, branches, and configuration.

Types:
- Local Repository
- Remote Repository (GitHub)

## Initializing a Repository

```bash
git init
```

Initializes a new Git repository by creating a hidden `.git` folder.

## Git Workflow

```
Working Directory
       │
   git add
       ▼
Staging Area
       │
 git commit
       ▼
Repository
```

## Git Status

```bash
git status
```

Shows:
- Current branch
- Modified files
- Untracked files
- Staged files

## Git Add

```bash
git add filename
git add .
```

Moves changes from the Working Directory to the Staging Area.

## Git Commit

```bash
git commit -m "Initial commit"
```

Creates a permanent snapshot of the staged changes.

A good commit message should be:
- Short
- Meaningful
- Written in imperative mood

Example:

```
Add login validation
Update README
Fix authentication bug
```

## Git Log

```bash
git log
git log --oneline
```

Displays the commit history of the repository.

### Key Points

- Git tracks every change made to a project.
- Commits create permanent snapshots of the project.
- The staging area allows selective commits.
- Meaningful commit messages improve project history.


# Part B – Working Directory, Staging Area & Repository

## Git Workflow

Git manages files using three areas:

```
Working Directory
       │
   git add
       ▼
Staging Area (Index)
       │
 git commit
       ▼
Local Repository
```

---

## Working Directory

The Working Directory contains the files that you are currently creating or modifying. Any changes made here are not yet tracked in the next commit.

---

## Staging Area (Index)

The Staging Area is a temporary area where changes are prepared before creating a commit.

Command:

```bash
git add <file_name>
```

or

```bash
git add .
```

Only the files in the staging area will be included in the next commit.

---

## Repository

The Repository stores all committed versions of the project. Every commit acts as a snapshot, allowing developers to restore previous versions whenever needed.

Command:

```bash
git commit -m "Commit message"
```

---

## Why Does Git Use a Staging Area?

The staging area gives developers control over what should be included in a commit.

Example:

Suppose you modified two files:

- `app.py`
- `README.md`

If only `app.py` is ready, you can stage only that file:

```bash
git add app.py
git commit -m "Add login feature"
```

The changes in `README.md` remain in the Working Directory and can be committed later.

---

## Benefits

- Better control over commits.
- Creates clean and meaningful commit history.
- Allows grouping related changes into a single commit.
- Prevents incomplete work from being committed.

---

## Key Points

- **Working Directory** → Contains current project files.
- **Staging Area** → Holds selected changes before committing.
- **Repository** → Stores permanent project history.
- `git add` moves changes to the staging area.
- `git commit` saves staged changes permanently.


# Part C – Git Diff & .gitignore

## Git Diff

`git diff` is used to compare changes in files. It helps developers review modifications before committing them.

### git diff

Shows the difference between the **Working Directory** and the **Staging Area**.

```bash
git diff
```

```
Working Directory
       │
   git diff
       ▼
Staging Area
```

Use this command to review unstaged changes.

---

### git diff --staged

Shows the difference between the **Staging Area** and the **Repository (last commit)**.

```bash
git diff --staged
```

```
Repository
      │
git diff --staged
      ▼
Staging Area
```

Use this command to review staged changes before committing.

---

## .gitignore

The `.gitignore` file tells Git which files and folders should **not** be tracked.

Example:

```text
*.log
.env
__pycache__/
.vscode/
```

Common files ignored:

- Log files (`*.log`)
- Environment files (`.env`)
- Python cache (`__pycache__/`)
- IDE settings (`.vscode/`)

### Why use `.gitignore`?

- Prevents committing sensitive information.
- Keeps the repository clean.
- Avoids tracking temporary or generated files.

> **Note:** `.gitignore` only prevents **new files** from being tracked. If a file has already been committed, it must first be removed from Git tracking using:

```bash
git rm --cached <file_name>
```

---

## Important Commands

```bash
git diff
git diff --staged
git status
git check-ignore -v <file>
git rm --cached <file>
```

---

## Key Points

- `git diff` shows **unstaged** changes.
- `git diff --staged` shows **staged** changes.
- `.gitignore` prevents unnecessary files from being tracked.
- `.gitignore` is **not** a security feature for already committed files.
- Use `git rm --cached` to stop tracking a file that has already been committed.


# Part D – Branching, Git Flow & Trunk-Based Development

## What is a Branch?

A branch is an independent line of development that allows developers to work on new features, bug fixes, or experiments without affecting the main codebase.

```
        main
         │
    ┌────┴────┐
    │         │
feature    hotfix
```

---

## Why Use Branches?

- Enables parallel development.
- Prevents changes from affecting the main branch.
- Makes collaboration easier.
- Allows testing before merging.

---

## Creating and Switching Branches

Create a new branch:

```bash
git branch feature/login
```

Switch to a branch:

```bash
git switch feature/login
```

Create and switch at the same time:

```bash
git switch -c feature/login
```

List all branches:

```bash
git branch
```

Delete a branch:

```bash
git branch -d feature/login
```

---

## Git Flow

Git Flow is a branching strategy that organizes development into different branch types.

```
              feature/*
                  │
                  ▼
             develop
                  │
             release/*
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
      main              develop
        │
     hotfix/*
        │
   ┌────┴────┐
   ▼         ▼
 main     develop
```

### Branch Types

- **main** – Production-ready code.
- **develop** – Main development branch.
- **feature/*** – New feature development.
- **release/*** – Preparing a software release.
- **hotfix/*** – Urgent production fixes.

---

## Trunk-Based Development

Trunk-Based Development is a branching strategy where developers frequently merge small changes into a single main branch (trunk).

```
Developer A ─┐
Developer B ─├──► main
Developer C ─┘
```

Feature branches, if used, are short-lived and merged quickly.

---

## Git Flow vs Trunk-Based Development

| Git Flow | Trunk-Based Development |
|-----------|-------------------------|
| Multiple long-lived branches | Single main/trunk branch |
| Separate develop branch | Frequent commits to main |
| Better for planned releases | Better for Continuous Integration |
| More structured workflow | Faster development cycle |

---

## Important Commands

```bash
git branch
git switch <branch-name>
git switch -c <branch-name>
git branch -d <branch-name>
```

---

## Key Points

- Branches allow independent development without affecting the main code.
- Feature branches are used for developing new features.
- Git Flow is suitable for structured release management.
- Trunk-Based Development focuses on frequent integration into the main branch.
- Using branches improves collaboration and reduces conflicts.


# Part E – Merge & Cherry-pick

## Git Merge

Git Merge is used to combine changes from one branch into another.

Example:

```
      main
        │
        ├───────────────┐
        │               │
    feature/login       │
        │               │
        └──────────────►│
                     Merge
```

Merge a branch into the current branch:

```bash
git merge feature/login
```

---

## Merge Conflict

A merge conflict occurs when the same part of a file is modified in different branches, and Git cannot automatically decide which change to keep.

Steps to resolve:
1. Open the conflicted file.
2. Edit and keep the required changes.
3. Stage the file.
4. Complete the merge.

Commands:

```bash
git add .
git commit
```

---

## Git Cherry-pick

`git cherry-pick` copies a specific commit from one branch and applies it to another branch without merging the entire branch.

Example:

```
main
 │
 ├───────────────► Commit A
 │
feature
 ├── Commit A
 ├── Commit B
 └── Commit C
```

Only **Commit B** can be copied to `main`.

Command:

```bash
git cherry-pick <commit-hash>
```

Find the commit hash:

```bash
git log --oneline
```

---

## Merge vs Cherry-pick

| Merge | Cherry-pick |
|--------|-------------|
| Combines the entire branch | Copies a specific commit |
| Preserves branch history | Copies selected changes only |
| Used after completing a feature | Used when only one commit is needed |

---

## Important Commands

```bash
git merge <branch-name>
git log --oneline
git cherry-pick <commit-hash>
```

---

## Key Points

- `git merge` combines two branches.
- Merge conflicts occur when the same code is modified in different branches.
- `git cherry-pick` copies a specific commit without merging the entire branch.
- Cherry-pick is useful for applying bug fixes or individual features to another branch.
```


# Part F – Rebase & Remote Repository

## Git Rebase

Git Rebase is used to move or replay commits from one branch onto another, creating a cleaner and more linear commit history.

```
Before Rebase:

main      A──B──C
              \
feature        D──E

After Rebase:

main      A──B──C
                  \
feature            D'──E'
```

Command:

```bash
git rebase main
```

---

## Merge vs Rebase

| Merge | Rebase |
|--------|--------|
| Creates a merge commit | No extra merge commit |
| Preserves complete history | Creates a linear history |
| Easier for team collaboration | Keeps commit history clean |

---

## Remote Repository

A Remote Repository is a repository hosted on platforms like **GitHub**, allowing developers to collaborate and back up their code.

Common remote operations:

Add a remote:

```bash
git remote add origin <repository-url>
```

View configured remotes:

```bash
git remote -v
```

Push changes:

```bash
git push -u origin main
```

Pull latest changes:

```bash
git pull origin main
```

Fetch changes without merging:

```bash
git fetch origin
```

---

## Important Commands

```bash
git rebase <branch-name>
git remote -v
git remote add origin <url>
git push -u origin main
git pull origin main
git fetch origin
```

---

## Key Points

- `git rebase` creates a cleaner, linear commit history.
- Use rebase before merging to reduce unnecessary merge commits.
- A remote repository enables collaboration and code backup.
- `git push` uploads local commits to the remote repository.
- `git pull` downloads and merges the latest changes from the remote repository.
```


# Part G – GitHub Repository Settings & Branch Protection

## GitHub Repository Settings

GitHub repository settings allow you to configure and manage your repository, including access control, branches, security, and integrations.

Common settings include:
- Repository visibility (Public/Private)
- Collaborator management
- Branch protection
- Security settings
- Webhooks and integrations

---

## Branch Protection

Branch Protection prevents direct changes to important branches (such as `main`) and ensures code quality before merging.

Common protection rules:
- Restrict direct pushes
- Require Pull Requests before merging
- Require code reviews
- Require status checks to pass
- Prevent force pushes
- Prevent branch deletion

```
Developer
    │
    ▼
Feature Branch
    │
Pull Request
    │
Code Review & Checks
    │
    ▼
Main Branch
```

---

## Why Use Branch Protection?

- Prevents accidental changes to the main branch.
- Improves code quality through reviews.
- Ensures tests pass before merging.
- Protects production-ready code.

---

## Important Steps

1. Open **Repository → Settings**.
2. Go to **Branches**.
3. Create a Branch Protection Rule.
4. Select the branch (e.g., `main`).
5. Enable required protection options.
6. Save the rule.

---

## Key Points

- Repository settings help manage access and security.
- Branch Protection safeguards important branches.
- Pull Requests and code reviews improve collaboration.
- Protected branches reduce the risk of introducing bugs into production.


# Part H – Pull Requests (PR)

## What is a Pull Request?

A Pull Request (PR) is a request to merge changes from one branch into another. It allows team members to review, discuss, and approve code before it is merged.

```
Feature Branch
      │
      ▼
Pull Request
      │
Code Review
      │
      ▼
Main Branch
```

---

## Pull Request Workflow

1. Create a feature branch.
2. Make changes and commit them.
3. Push the branch to GitHub.
4. Create a Pull Request.
5. Review and approve the changes.
6. Merge the Pull Request.
7. Delete the feature branch (optional).

---

## Benefits of Pull Requests

- Improves code quality through reviews.
- Encourages team collaboration.
- Helps identify bugs before merging.
- Maintains a clean project history.

---

## Important Commands

Create and push a new branch:

```bash
git switch -c feature-branch
git push -u origin feature-branch
```

After the Pull Request is approved:

```bash
git switch main
git pull origin main
```

---

## Key Points

- A Pull Request is used to merge code after review.
- Team members can review, comment, and approve changes.
- PRs improve collaboration and code quality.
- Feature branches are typically merged into the `main` branch using Pull Requests.


# Part I – GitHub Desktop & VS Code Source Control

## GitHub Desktop

GitHub Desktop is a graphical user interface (GUI) that simplifies Git operations without using the command line.

Features:
- Clone repositories
- Commit changes
- Create and switch branches
- Push and pull changes
- Resolve merge conflicts
- View commit history

---

## VS Code Source Control

VS Code has built-in Git support through the **Source Control** panel.

Features:
- View changed files
- Stage and unstage changes
- Commit changes
- Create and switch branches
- Push and pull from GitHub
- Resolve merge conflicts

```
Edit Files
     │
     ▼
Source Control
     │
Stage Changes
     │
Commit
     │
Push to GitHub
```

---

## Advantages

- Easy-to-use graphical interface.
- No need to remember Git commands.
- Faster for beginners.
- Integrated with GitHub repositories.
- Simplifies branch management and commits.

---

## Key Points

- GitHub Desktop is a GUI application for Git and GitHub.
- VS Code provides built-in Git integration through Source Control.
- Both tools support commits, branches, push, pull, and merge operations.
- GUI tools make Git easier while still using the same Git concepts.


# Part J – Git Revert & Git Reset

## Git Revert

`git revert` is used to undo a committed change by creating a **new commit** that reverses the changes. It does not remove commit history.

Command:

```bash
git revert <commit-hash>
```

Use when:
- Undoing changes in a shared repository.
- Preserving commit history.

---

## Git Reset

`git reset` is used to move the current branch to a previous commit. It can remove commits and staged changes depending on the option used.

### Soft Reset

Moves the HEAD to a previous commit but keeps changes staged.

```bash
git reset --soft <commit-hash>
```

### Mixed Reset (Default)

Moves the HEAD to a previous commit and unstages the changes, but keeps them in the working directory.

```bash
git reset --mixed <commit-hash>
```

### Hard Reset

Moves the HEAD to a previous commit and permanently deletes all changes after that commit.

```bash
git reset --hard <commit-hash>
```

> **Warning:** `git reset --hard` permanently removes uncommitted changes.

---

## Revert vs Reset

| Git Revert | Git Reset |
|------------|-----------|
| Creates a new commit | Removes or moves commits |
| Preserves commit history | Can rewrite history |
| Safe for shared repositories | Best for local changes |

---

## Important Commands

```bash
git revert <commit-hash>
git reset --soft <commit-hash>
git reset --mixed <commit-hash>
git reset --hard <commit-hash>
```

---

## Key Points

- Use **git revert** to safely undo commits in shared repositories.
- Use **git reset** to modify or remove local commit history.
- Avoid using `git reset --hard` unless you are sure the changes are no longer needed.


# Part K – GitHub Copilot & Git Flow Capstone

## GitHub Copilot

GitHub Copilot is an AI-powered coding assistant developed by GitHub and OpenAI. It helps developers write code faster by providing real-time code suggestions and completions.

### Features

- Code completion
- Function generation
- Code explanation
- Test case generation
- Documentation assistance

### Benefits

- Increases developer productivity.
- Reduces repetitive coding tasks.
- Helps learn new programming languages and frameworks.
- Improves code quality with intelligent suggestions.

---

## Git Flow Capstone

The Git Flow Capstone demonstrates a complete Git workflow by using feature branches, commits, Pull Requests, and merging.

### Workflow

```
Create Repository
       │
Create Feature Branch
       │
Make Changes & Commit
       │
Push to GitHub
       │
Create Pull Request
       │
Code Review
       │
Merge to Main
```

---

## Git Workflow Used

1. Initialize the repository.
2. Create a feature branch.
3. Make changes and commit them.
4. Push the branch to GitHub.
5. Create a Pull Request.
6. Review and merge the Pull Request.
7. Update the local repository.

---

## Important Commands

```bash
git switch -c feature-branch
git add .
git commit -m "Add new feature"
git push -u origin feature-branch
git pull origin main
```

---

## Key Points

- GitHub Copilot is an AI coding assistant that improves development speed.
- Git Flow organizes development using branches and Pull Requests.
- A complete Git workflow includes branching, committing, reviewing, and merging.
- Following Git best practices improves collaboration and maintains a clean project history.


