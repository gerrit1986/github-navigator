from django.http import HttpResponse
from django.template.loader import get_template
from api import get_results


def request(request):
    """
    Takes in a request and a query. Pulls content from the API according to the
    query and displays it to the page.

    :param request: a request by the user from the URL.
    :param query: a query given by the user via URL request.
    """
    search_term = request.GET.get('search_term')
    template = get_template('template.html')
    query = unicode(search_term)
    results = get_results(search_term)

    try:
        content = template.render({'search_term': search_term,
                                   'results': results, })
    except IndexError:
        return HttpResponse("No results for query '" + str(query) +
        "' or something went wrong.")

    return HttpResponse(content)
