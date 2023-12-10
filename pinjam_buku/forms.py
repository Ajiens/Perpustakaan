from django.forms import ModelForm
from django import forms
from pinjam_buku.models import Borrow

class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = ["tanggal_pengembalian"]