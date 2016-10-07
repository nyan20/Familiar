from django.conf.urls import url, include

from myapp.familia.views import index, familia_view, familia_list, familia_edit, familia_delete, FamiliaList, FamiliaCreate, FamiliaUpdate, FamiliaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', FamiliaCreate.as_view(), name='familia_crear'),
    url(r'^listar$', FamiliaList.as_view(), name='familia_listar'),
    url(r'^editar/(?P<pk>\d+)/$', FamiliaUpdate.as_view(), name='familia_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', FamiliaDelete.as_view(), name='familia_eliminar'),
]
