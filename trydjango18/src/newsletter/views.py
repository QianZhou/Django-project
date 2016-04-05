from django.shortcuts import render

from .forms import ContactForm,SignUpForm

# Create your views here.
def home(request):
    title='Welcome'
    #if request.user.is_authenticated():
    #    title="My Title %s" %(request.user)
    
    
    #add a form
    #if request.method=="POST":
    #    print request.POST
    
   
    
    form =SignUpForm(request.POST or None)
    context={
        "title":title,
        "form":form
    }
    
    if form.is_valid():
        #form.save()
        #print request.POST['email']#not recommended
        instance=form.save(commit=False)
        full_name=form.cleaned_data.get('full_name')
        if not full_name:
            full_name="New full name"
        instance.full_name=full_name    
        #if not instance.full_name:
        #    instance.full_name="Justine"
        instance.save()
        #print instance.email
        #print instance.timestamp
        
        context={
        "title":"Thank you"
        }
    return render(request,"home.html",context)

def contact(request):
    form =ContactForm(request.POST or None)
    if form.is_valid():
        for key,value in form.cleaned_data.iteritems():
            print key,value
            #print form.cleaned_data.get(key)
        #full_name=form.cleaned_data.get('full_name')
        # email=form.cleaned_data.get('email')
        #message=form.cleaned_data.get('message')
        #print full_name,email,message
        
    context={
          "form":form
    }
    return render(request,"forms.html",context)