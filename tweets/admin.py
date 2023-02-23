from django.contrib import admin
from tweets.models import Tweet

# Register your models here.
@admin.register(Tweet)
class Tweet_Class(admin.ModelAdmin):
    list_display= ['author', 'created_at', 'updated_at', 'content']
    date_hierarchy= 'created_at'
    actions_on_top= True # this creates action on the top
    actions_on_bottom= True # this creates action on the bottom
    actions_selection_counter= True 
    list_filter= ['author', 'created_at', 'updated_at'] # this will create a filter box in the tweets admin page.
    search_fields= ['author', 'content'] # this will create a fuctionality to searchbar that author and content can be search the tweets.
    # list_select_related= True
    # list_editable= ['author', 'created_at', 'updated_at', 'content'] 
    save_as= True
    save_as_continue= True
    save_on_top= True
    save_on_bottom= True
    # preserve_filters= True
    # exclude= ['author', 'updated_at']
    
    
    
    



# admin.site.register(Tweet, Tweet_Class)
