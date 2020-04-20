from flask import Flask, render_template,request,abort
import requests
import json
import os

app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("home.html")

@app.route('/busqueda',methods=["GET","POST"])
def busqueda():
    ciudad=request.form.get("ciudad")
    pais=request.form.get("pais")
    radio=request.form.get("radio")
    tipo=request.form.get("tipo")
    err="No se ha encontrado ninguna vía de esa modalidad"
    mapa=True
    try:

        mountainkey=os.environ['MountainProject']
        mapboxkey=os.environ['Mapbox']
        yandexkey=os.environ['Yandex']
        yandex={"key":yandexkey,"text":pais,"lang":"es-en"}
        traduccion=requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',params=yandex)
        pais=traduccion.json()["text"][0]
        link=str("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ciudad+".json")
        mapbox={"access_token":mapboxkey}
        r=requests.get(link,params=mapbox)
        if r.status_code == 200:
            doc=r.json()
            features=[]
            for lugares in doc["features"]:
                for regiones in lugares["context"]:
                    if regiones["id"].find("country")!=-1 and regiones["text"]==pais:
                        latitud=str(lugares["center"][1])
                        longitud=str(lugares["center"][0])

        radio=str(float(radio)/1.609)
        mountainproject={"lat":latitud,"lon":longitud,"maxDistance":radio,"key":mountainkey}
        r=requests.get('https://www.mountainproject.com/data/get-routes-for-lat-lon',params=mountainproject)
        if r.status_code == 200:
            doc=r.json()
            for p in doc["routes"]:
                if tipo == "Sport":
                    if p["type"]==tipo:
                        lat=p["latitude"]
                        lon=p["longitude"]
                        lugar=p["name"]
                elif tipo == "Trad":
                    if p["type"]==tipo:
                        lat=p["latitude"]
                        lon=p["longitude"]
                        lugar=p["name"]
                elif tipo == "Boulder":
                    if p["type"]==tipo:
                        lat=p["latitude"]
                        lon=p["longitude"]
                        lugar=p["name"]
                else:
                    lat=p["latitude"]
                    lon=p["longitude"]
                    lugar=p["name"]
                try:
                    features.append({"type": "Feature","geometry": {"type": "Point","coordinates": [lon, lat]},"properties": {"title": lugar,"icon": "marker"}})
                except:
                    mapa=False
    except:
        abort(404)
    return render_template("busqueda.html",features=features,err=err,latitud=latitud,longitud=longitud,mapboxkey=mapboxkey,destino=ciudad)    

@app.route('/noticias',methods=["GET"])
def noticias():
    NewsKey=os.environ['NewsApi']
    NewsParams={"apiKey":NewsKey,"q":"ifsc climbing","sortBy":"popularity"}
    listanoticias=[]
    tendencia=[]
    Contador=1
    try:
        noticias=requests.get('https://newsapi.org/v2/everything',params=NewsParams)
        if noticias.status_code == 200:
            doc=noticias.json()
            tendencia.append(doc["articles"][0]["title"])
            tendencia.append(doc["articles"][0]["description"])
            tendencia.append(doc["articles"][0]["url"])
            tendencia.append(doc["articles"][0]["urlToImage"])
            for i in range(1,len(doc["articles"])):
                noticia=[]
                noticia.append(doc["articles"][i]["title"])
                noticia.append(doc["articles"][i]["description"])
                noticia.append(doc["articles"][i]["url"])
                noticia.append(doc["articles"][i]["urlToImage"])
                noticia.append(doc["articles"][i]["source"]["name"])
                listanoticias.append(noticia)
        numnoticias=len(listanoticias)
    except:
        abort(404)
    return render_template('noticias.html',tendencia=tendencia,listanoticias=listanoticias,numnoticias=numnoticias,Contador=Contador)

@app.route('/busqueda/blablacar',methods=["GET","POST"])
def blablacar():
    destino=request.form.get("destino")
    origen=request.form.get("origen")
    blablakey=os.environ['Blablacar']
    listaviajes=[]
    try:
        opciones={"locale":"es_ES","accept":"application/json","fn":origen,"tn":destino,"_format":"json","cur":"EUR","sort":"trip_price","order":"asc","key":blablakey}
        rutas=requests.get('https://public-api.blablacar.com/api/v2/trips',params=opciones)
        if rutas.status_code == 200:
            doc=rutas.json()

            for viajes in doc["trips"]:
                ruta=[]
                precio=viajes["price_with_commission"]["value"]
                sitioslibres=viajes["seats_left"]
                sitiostotales=viajes["seats"]
                FechaSalida=viajes["departure_date"]
                CiudadQuedada=viajes["departure_place"]["city_name"]
                DireccionQuedada=viajes["departure_place"]["address"]

                ruta.append(precio)
                ruta.append(sitioslibres)
                ruta.append(sitiostotales)
                ruta.append(FechaSalida)
                ruta.append(DireccionQuedada)
                try:
                    MarcaCoche=str(viajes["car"]["make"]+" "+viajes["car"]["model"])
                    ruta.append(MarcaCoche)
                except:
                    ruta.append("???")

                ruta.append(viajes["links"]["_front"])
                listaviajes.append(ruta)
        numviajes=len(listaviajes)
    except:
        abort(404)
    return render_template("blablacar.html",numviajes=numviajes,listaviajes=listaviajes,destino=destino,origen=origen)

@app.route('/youtube',methods=["GET","POST"])
def canales():
    link='https://www.googleapis.com/youtube/v3/search'
    youKey=os.environ['Youtube']
    Canales=['UC2MGuhIaOP6YLpUx106kTQw','UC_gSotrFVZ_PiAxo3fTQVuQ','UC8eNyF9eYwgr_K-Nl4gSHWw','UCgtOMaHBiYvsRYZ77utf8FQ','UCt_aqQDpGzyRDALTVyBe7xg']
    listaCanales=[]
    videosCanal={}
    tresvideos=[]
    Quota=True
    try:
        for identificador in Canales:
            youtubeparams={"part":"snippet","maxResults":"3","order":"date","type":"video","key":youKey,"channelId":identificador}
            videos=requests.get(link,params=youtubeparams)
            if videos.status_code == 200:
                lista=videos.json()
                videosCanal={}
                tresvideos=[]
                for video in lista["items"]:
                    info=[]
                    videoid=video["id"]["videoId"]
                    titulo=video["snippet"]["title"]
                    miniatura=video["snippet"]["thumbnails"]["high"]["url"]
                    Canal=video["snippet"]["channelTitle"]
                    info.append(videoid)
                    info.append(titulo)
                    info.append(miniatura)
                        
                    tresvideos.append(info)

                videosCanal={"videos":tresvideos,"nombre":Canal}
                listaCanales.append(videosCanal)
            elif videos.status_code == 403:
                Quota=False
    except:
        abort(404)
    return render_template("Youtube.html",listaCanales=listaCanales,Quota=Quota)

app.run('0.0.0.0',8080,debug=True)
