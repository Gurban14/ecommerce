from main.models import *

def context_data(request):
  all_cat = Category.objects.all()
  info = Info.objects.first()
  s_accounts = Social_account.objects.all() 

  if request.user.is_authenticated:
    cart, created = Cart.objects.get_or_create(user = request.user, is_ordered = False)
  else:
    cart = None


  return {
    'all':all_cat,
    'info':info,
    's_accs':s_accounts,
    'cart': cart
  }

   