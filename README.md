**Update on 11/7/2021**

We have uploaded the exercises in each chapter.

We firstly completed the version control and toy example in the `master` branch. Then we realized we should set a new branch for every chapter's exercise to avoid mistakes. That's why we have many branches. 

Today, for convenience, I have merged all branches into a new branch `main` except `feature-1` since it will incur conflict between files in the toy example.

**Update on 11/7/2021** 

Sorry, I noticed I made a mistake in the toy example. I fixed it in the `feature-1`. It will not affect the `main` branch. Now the branch tree looks like below:

~~~shell
G:\github\dtff1>git log --oneline --graph --all
* 43b7ea1 (HEAD -> main, origin/main) updates on README.md
* c223b45 update on README.md
* a32173e Merge all branches into main
*   165e0ba Merge branch 'writing_with_latex' into main
|\
| * 0e7698e (origin/writing_with_latex, writing_with_latex) writing with latex
| * 8c9f578 added dataManagement
* |   3a5902d Merge branch 'web-api' into main
|\ \
| * | db12b5a (origin/web-api, web-api) added web-api
| |/
* |   04e4bcd Merge branch 'data_management' into main
|\ \
| * | fb96ee2 (origin/data_management, data_management) added data_management
| |/
* / ee49b5d (origin/project_directory, project_environment) project directory
|/
| * 01bf42a (origin/feature-1, feature-1) This line is bad
|/
* 09117db (origin/master, master) finally ok
* d2c4d24 chg line to bad in feature-1
*   a1ed67c merge, conflict resolved
|\
| * 8408ffe bob
| * 2f85b7e bob
| * 85bb57d bob
* | 6b4f505 This #2 line is ok
|/
* 7bb992a alice
* 16fe768 init
* 29addbf I am Alice
* 1e7686c init
* b837c37 Revert "first-working"
* 0307565 first-working
* d69078d a good change
* 2c82355 init
* 4891c66 Init
* b7ff72f Init
~~~

