# Articles & Sections

In a new test project, or in the test project you already have set up:

Have an Article model as well as one called Section
Both sections and articles have a title field, a simple charfield.
We need a relationship between the two. Practice the implimentation of a ForeignKey.
An article object can have 1 section, but a section object can have many articles.
Try to figure out where an FK has to go and add it to the necessary model.

Register the Section and the Article models in the django admin panel so you can add/edit/remove them.
Create 3 sections, with titles 'alpha', 'bravo', 'charlie', and create a handful of articles for each section

Now create a view called Homepage, and make it a ListView. It lists Articles
The initial queryset for the listview should filter based on the section alpha.
Now, add 2 more querysets to the context. Articles filtered by bravo and charlie.

In the template, have 3 seperate lists. Each of them looping through the alpha, bravo and charlie lists.
For each article in the lists, have each article title display as a <p> element, and make them all have a simple black border-bottom
Remove the border from the last <p> of each list, so the at the bottom of the list there is no line
Define a background colour for each <p> that is an odd index, and a different one for the even ones. (So the first, third etc. <p> all have a different background color to the second, fourth)


This exercise should demonstrate:
 - models and simple FK relationships
 - admin registration
 - class based views
 - basic django queryset filtering
 - adding variables to the context
 - django template forloops
 - basic html/css 
