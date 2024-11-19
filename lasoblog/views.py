 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Newblog
from .forms import NewBlogForm ,BlogForm # We'll create this form in the next step
 
def add_blog(request):
    if request.method == "POST":
        form = NewBlogForm(request.POST, request.FILES)  # Handle form data and file uploads
        if form.is_valid():
            form.save()  # Save the blog to the database
            return redirect('home')  # Redirect to the homepage or another page
    else:
        form = NewBlogForm()  # Display an empty form
    return render(request, 'dist/add_blog.html', {'form': form})


def home(request):
      blogs=Newblog.objects.all()
      return render(request,"dist/index.html",{"blog":blogs})    
def addblog(request,pk):
      blogs=Newblog.objects.get(id=pk)
      return render(request,"dist/addblog.html",{"blog":blogs})    

def delete_blog(request, pk):
    blog = get_object_or_404(Newblog, pk=pk)  # Get the blog by its primary key
    if request.method == "POST":  # If the form is submitted
        blog.delete()  # Delete the blog
        return redirect('home')  # Redirect to homepage or another page after deletion
    return render(request, 'dist/delete_blog.html', {'blog': blog})  

def update_blog(request, pk):
    blog = get_object_or_404(Newblog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after updating
    else:
        form = BlogForm(instance=blog)
    return render(request, 'dist/update_blog.html', {'form': form, 'blog': blog})