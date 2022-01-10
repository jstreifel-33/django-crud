# Django Crud

An exploration of CRUD using Django models.

## Deployment

This site is not deployed anywhere in the cloud. Please feel free to fork or clone the repository for local deployment.

## Submission

PR: [Working Branch #1](http.cats)

## Feature Tasks

- [x] Create snacks_crud_project Django project
- [x] Create snacks app
- [x] Create Snack model
  - [x] title field
  - [x] purchaser field
  - [x] description field
  - [x] Register model with admin
- [x] Create SnackListView that extends appropriate generic view
  - [x] associated url path is an empty string
- [x] Create SnackDetailView that extends appropriate generic view
  - [x] associated url path is `<int:pk>/`
- [x] Create SnackCreateView that extends appropriate generic view
  - [x] associated url path is `create/`
- [x] Create SnackUpdateView that extends appropriate generic view
  - [x] associated url path is `<int:pk>/update/`
- [x] Create SnackDeleteView that extends appropriate generic view
  - [x] associated url path is `<int:pk>/delete/`
- [x] Add urls to support all views, with appropriate names
- [x] Add templates to support all views
- [x] Add navigation links in appropriate locations to access all pages
- [x] Make all necessary changes to project level files for project to run
  - [x] In other words, make it work
