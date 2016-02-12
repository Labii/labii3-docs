from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, resolve
from django.conf import settings
from accounts.decorators import track_url
from metrics.tasks import add_view_count
from common.backend import id2eid, writeIntoDB, es2s
from docs.models import *
from sections.models import Sections

def get_md(filename):
	md = None
	title = None
	did = None
	desb = None
	# prepare the id
	if Docs.objects.filter(titlename=filename).exists():
		did = Docs.objects.get(titlename=filename).id
	else:
		d = {}
		d["titlename"] = filename
		dd = writeIntoDB(Docs,d)
		did = dd.id
	# get the file content
	with open("%s/docs/docs/%s" % (settings.BASE_DIR,filename),"r") as newfile:
		md = newfile.read()
	tmp = md.replace("\r","").split("\n")
	if len(tmp) > 0:
		title = tmp[0].replace("\r","").replace("#","")
	i = 1
	while desb == None:
		if tmp[i] != "":
			desb = tmp[i]
		i = i + 1
	# links
	link = ""
	if filename.find("eln_") != -1:
		link = "<a href='%s'>Labii ELN</a>" % reverse("notes_support")
	else:
		assert False
	return (did,title,link,desb,md)

def schema_docs(request,data):
	template = 'tlr.html'
	if not "meta_description" in data:
		data["meta_description"] = "Documentation for Labii apps."
	data["brand"] = "Docs"
	if not "title" in data:
		data["title"] = "Docs"
	data["tlr_sb"] = 'docs/sidebar.html'
	#data["tlr_js_bottom"] = "labii/js_bottom.html"
	if "template" in data:
		template = data["template"]
	return render_to_response(template,data,context_instance=RequestContext(request))

def docs_home(request):
	data = {}
	data["sections"] = Sections.objects.filter(dbname='docs_home',dbid=0).order_by("order")
	data["eedit"] = es2s('false')
	data["tlr_content"] = 'docs/home.html'
	data["fluid"] = 'true'
	return schema_docs(request,data)

def docs_page(request,filename):
	data = {}
	(data["did"],data["title"], data["link"], data["desb"], data["md"]) = get_md(filename)
	data["edid"] = id2eid(data["did"])
	data["meta_description"] = data["desb"]
	add_view_count(request,'docs',data["did"],'docs_page')
	data["tlr_content"] = 'docs/view.html'
	data["filename"] = filename
	return schema_docs(request,data)

def docs_view(request,filename):
	data = {}
	(data["did"],data["title"], data["link"], data["desb"], data["md"]) = get_md(filename)
	data["edid"] = id2eid(data["did"])
	data["filename"] = filename
	add_view_count(request,'docs',data["did"],'docs_view')
	return render_to_response('docs/view.html',data,context_instance=RequestContext(request))

def docs_modalview(request,filename):
	data = {}
	(data["did"],data["title"], data["link"], data["desb"], data["md"]) = get_md(filename)
	data["edid"] = id2eid(data["did"])
	data["filename"] = filename
	add_view_count(request,'docs',data["did"],'docs_modalview')
	return render_to_response('docs/modalview.html',data,context_instance=RequestContext(request))