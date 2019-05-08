from django.shortcuts import render
from .models import Member
from  django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
# def index(request):
#     profiles =Member.objects.all()
#     return render(request,'tonnieapp/index.html',{'profiles':profiles})
class MemberListView(ListView):
    model = Member
    template_name = 'tonnieapp/index.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        query=self.request.GET.get('q')
        if(query):
            return Member.objects.filter(name__icontains=query)
        else:
            return Member.objects.all()


class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'

class MemberUpdateView(UpdateView):
    model = Member
    fields = '__all__'

class MemberDeleteView(DeleteView):
    model = Member
    success_url = '/'