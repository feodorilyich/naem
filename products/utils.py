from products.models import Product
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery, SearchHeadline
from django.db.models import Q

def q_search(query):
    if query.isdigit() and len(query) <= 7:
        return Product.objects.filter(id=int(query))
    vector = SearchVector("name","description")
    q_obj = SearchQuery(query)

    query_res =  Product.objects.annotate(rank=(SearchRank(vector,q_obj))).filter(rank__gt=0).order_by("-rank")

    query_res = query_res.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel = "<span style='background-color: yellow;'>"
        )
    )
    query_res = query_res.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel = "<span style='background-color: yellow;'>"
        )
    )

    return query_res
   

    # keywords = [word for word in query.split() if len(word)>3]

    # q_objects = Q()

    # for word in keywords:
    #     q_objects |= Q(description__contains=word)
    #     q_objects |= Q(name__contains=word)

    # return Product.objects.filter(q_objects)