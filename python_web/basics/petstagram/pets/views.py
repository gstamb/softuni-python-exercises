from django.shortcuts import render, redirect
from django.urls import reverse
from pets.forms import CommentForm, EditPetForm

from pets.models import Pet, Like, Comment


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pet_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            # you can also pass comments as context instead of loading comments as a set in the view
            # 'comments': Comment.objects.filter(pet=pet_obj)
            'form': CommentForm(),
        }
        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(pet=pet, text=form.cleaned_data['text'])
            comment.save()
            return redirect('pet details or comment', pk)
        else:       
            context = {
                'pet': pet,
                'form': form,
            }
            return render(request, 'pet_detail.html', context)
        
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(comment=str(pk))
    like.like = pet
    like.save()
    return redirect('pet details or comment', pk)
 
def delete_pet(request,pk):  
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    
    else:
        context = {
        'pet': pet
        }  
        return render(request, 'pet_delete.html', context)
            
def persist_pet(request, pet=None, template_name='pet_edit.html'):
    if pet is None:
        pet = Pet()   
    
    if request.method == 'GET':
        form = EditPetForm(instance=pet)
        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, template_name, context)
    
    else:
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.id)
        else:
            context = {
                'pet': pet,
                'form': form,
            }
            return render(request, template_name, context)
 

def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)        
    return persist_pet(request, pet, 'pet_edit.html')
 
def create_pet(request):
    return persist_pet(request, template_name='pet_create.html')



# def edit_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)    
#     if request.method == 'GET':
#         form = EditPetForm(instance=pet)
#         context = {
#             'pet': pet,
#             'form': form,
#         }
#         return render(request, 'pet_edit.html', context)
    
#     else:
#         form = EditPetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('pet details or comment', pet.id)
#         else:
#             context = {
#                 'pet': pet,
#                 'form': form,
#             }
#             return render(request, 'pet_edit.html', context)
 
 
# def create_pet(request):
#     if request.method == 'GET':
#         form = EditPetForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'pet_create.html', context)
    
#     else:
#         form = EditPetForm(request.POST, instance=Pet())
#         if form.is_valid():
#             new_pet_instance = form.save()
#             return redirect('pet details or comment', new_pet_instance.id)
#         else:
#             context = {
#                 'form': form,
#             }
#             return render(request, 'pet_create.html', context)
      


