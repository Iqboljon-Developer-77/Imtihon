from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat.errors import messages

from .forms import AddReviewForm, ReviewUpdateForm
from .models import Computers, Review, CategoryComputer
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.


class ComputerListView(View):
    def get(self, request):
        computers = Computers.objects.all().order_by('-id')
        search_query = request.GET.get('search')

        if search_query:
            computers = computers.filter(
                Q(title__icontains=search_query)
            )
            if not computers:
                messages.warning(request, 'No computers found matching your search.')

        return render(request, 'computer/computer_list.html', {'computers': computers})
# class BookListView(ListView):
#     model = Books
#     template_name = 'book/book_list.html'
#     context_object_name = 'book'

class ComputerDetailView(View):
    def get(self, request, pk):
        computer = Computers.objects.get(pk=pk)
        reviews = Review.objects.filter(computer_id=pk)
        print(reviews)
        context = {
            'computer': computer,
            'reviews': reviews
        }
        return render(request, 'computer/computer_detail.html', context=context)


class ComputerCreateView(CreateView):
    model = Computers
    template_name = 'computer/computer_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:computer-list')


# class ComputerDeleteView(DeleteView):
#     model = Computers
#     template_name = 'computer/computer_delete.html'
#     success_url = reverse_lazy('products:computer-list')


class ComputertDeleteView(View):
    def get(self, request, pk):
        computer = Computers.objects.get(pk=pk)
        return render(request, 'computer/computer_delete.html', {'computer': computer})

    def post(self, request, pk):
        product = Computers.objects.get(pk=pk)
        product.delete()
        # messages.success(request, 'Product deleted successfully.')
        return redirect('products:computer-list')  # Assuming you have a URL name 'list' for listing products


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        computer = Computers.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'computer': computer,
            'add_review_form': add_review_form
        }
        return render(request, 'computer/add_review.html', context=context)

    def post(self, request, pk):
        computer = Computers.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                computer=computer,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )

            review.save()
            return redirect('products:computer-detail', pk=pk)


class ReviewUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        update_review_form = ReviewUpdateForm(instance=review)
        context = {
            'update_review_form': update_review_form
        }
        return render(request, 'computer/review_update.html', context=context)

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        update_review_form = ReviewUpdateForm(request.POST, instance=review)
        if update_review_form.is_valid():
            update_review_form.save()
            return redirect('products:computer-detail', pk=review.computer.pk)
        else:
            return render(request, 'computer/review_update.html', {'update_review_form': update_review_form})

class CategoryListView(LoginRequiredMixin, ListView):
    def get(self, request):
        category = CategoryComputer.objects.all()

        return render(request, 'computer/products.html', {'categorys': category})

