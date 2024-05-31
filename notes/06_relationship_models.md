we can create different kinds of relationships.

one to many relation
```python
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVariety, on_delete=models.CASCADE, related_name="reviews"
    )
```


many to many relations
```python
chai_varieties = models.ManyToManyField(to=ChaiVariety, related_name="stores")
```

one to one relation
```python
chai = models.OneToOneField(
        ChaiVariety, on_delete=models.CASCADE, related_name="certificate"
    )
```

**Note:** In above examples, `related_name` is used to refer the entity outside the class

If we want to add the review along with tea adding, we use TabularInline. i.e. shown one below another
```python
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2
```

To add the chai varieties along with store i.e. shown horizontally
```python
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("chai_varieties",)
```