# Changelog for django-wordpress

## 0.9.6

* allow hyphens in author usernames

## 0.9.5

* fix error handling in author archive when author does not exist

## 0.9.4

* prefetch term objects when getting taxonomies

## 0.9.3

* add child post cache

## 0.9.2

* add tag cache

## 0.9.1

* fix call to Preview view

## 0.9

* add post_archive_author template
* change default templates (except year archive) to extend from post_archive template

## 0.8

* add User to context when displaying author archive

## 0.7

* honor order of term taxonomy relationships

## 0.6

* remove wp_options.blog_id field as it no longer exists in WP 3.5.x

## 0.5

* Django 1.5 support
* fixed incorrect lookups for term views
* added Post.objects.from_path(path) method to load post from WordPress-style URL path

## 0.4

* add class-based views
* deprecate method-based views

## 0.3

* fix multi-database support

## 0.2

* disabled support for Link.category_id and Post.category_id (WordPress 3.x)
* added the *WP_DATABASE* setting to specify which database the wordpress content is coming from
* added mapping for TermTaxonomyRelationship so there is no more hand-crafted SQL being run
* PostManager.term() now supports multiple terms
* added Term.get_absolute_url()
* ensured that WordPress tables are not created or deleted by Django by marking them as unmanaged

Thanks to [twig](https://github.com/twig) for this release!

## 0.1

*   initial release
