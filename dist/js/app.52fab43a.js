(function(e){function t(t){for(var n,a,c=t[0],s=t[1],u=t[2],l=0,d=[];l<c.length;l++)a=c[l],o[a]&&d.push(o[a][0]),o[a]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(e[n]=s[n]);p&&p(t);while(d.length)d.shift()();return i.push.apply(i,u||[]),r()}function r(){for(var e,t=0;t<i.length;t++){for(var r=i[t],n=!0,c=1;c<r.length;c++){var s=r[c];0!==o[s]&&(n=!1)}n&&(i.splice(t--,1),e=a(a.s=r[0]))}return e}var n={},o={app:0},i=[];function a(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,a),r.l=!0,r.exports}a.m=e,a.c=n,a.d=function(e,t,r){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(a.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)a.d(r,n,function(t){return e[t]}.bind(null,n));return r},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],s=c.push.bind(c);c.push=t,c=c.slice();for(var u=0;u<c.length;u++)t(c[u]);var p=s;i.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"034f":function(e,t,r){"use strict";var n=r("64a9"),o=r.n(n);o.a},"3b5e":function(e,t,r){"use strict";var n=r("4fc0"),o=r.n(n);o.a},"4fc0":function(e,t,r){},"56d7":function(e,t,r){"use strict";r.r(t);r("cadf"),r("551c"),r("f751"),r("097d");var n=r("2b0e"),o=r("14ba"),i=r.n(o),a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("h1",[e._v("Olá, obrigado por me ajudar na validação do meu TCC, basta seleciona qual vitrine abaixo você mais gosta")]),r("h2",[e._v("O primeiro produto da vitrine é o produto referencia, os outros são recomendações")]),r("carousel",{attrs:{perPage:this.carousel.perPage}},[r("slide",[r("selection",{attrs:{option:"A"}})],1),e._l(e.recsA,function(e){return r("slide",{key:e.id},[r("product",{attrs:{img:e.image,name:e.name,price:e.price}})],1)})],2),r("carousel",{attrs:{perPage:this.carousel.perPage}},[r("slide",[r("selection",{attrs:{option:"B"}})],1),e._l(e.recsB,function(e){return r("slide",{key:e.id},[r("product",{attrs:{img:e.image,name:e.name,price:e.price}})],1)})],2)],1)},c=[],s=r("0a63"),u=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"card"},[r("img",{staticStyle:{width:"100%"},attrs:{src:e.img,alt:"Denim Jeans"}}),r("h3",[e._v(e._s(e.name))]),r("p",{staticClass:"price"},[e._v("$"+e._s(e.price))])])},p=[],l={name:"Product",props:{img:String,name:String,price:String}},d=l,f=(r("8885"),r("2877")),v=Object(f["a"])(d,u,p,!1,null,"3394b144",null),h=v.exports,m=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"card"},[r("p",[r("button",{on:{click:function(t){return e.sendEvent()}}},[e._v("Opção "+e._s(e.option))])])])},g=[],b=r("bc3a"),_={name:"Select",props:{option:String},methods:{sendEvent:function(){var e={cookie:document.cookie,option:this.$options.propsData.option};b.post("https://radiant-springs-66987.herokuapp.com/event",e).then(function(){alert("Muito Obrigado!")})}}},y=_,O=(r("3b5e"),Object(f["a"])(y,m,g,!1,null,"3de72251",null)),S=O.exports,P=r("bc3a"),j={components:{Carousel:s["Carousel"],Slide:s["Slide"],Product:h,Selection:S},data:function(){return{recFor:"B005PB2T0S",recsA:[],recsB:[],carousel:{perPage:6}}},mounted:function(){var e=this;P.get("http://radiant-springs-66987.herokuapp.com/rec/pln/".concat(this.recFor)).then(function(t){e.recsA=t.data.recs}),P.get("http://radiant-springs-66987.herokuapp.com/rec/original/".concat(this.recFor)).then(function(t){e.recsB=t.data.recs})}},k=j,w=(r("034f"),Object(f["a"])(k,a,c,!1,null,null,null)),x=w.exports;n["a"].config.productionTip=!1,n["a"].use(i.a),new n["a"]({render:function(e){return e(x)}}).$mount("#app")},"64a9":function(e,t,r){},8885:function(e,t,r){"use strict";var n=r("fd16"),o=r.n(n);o.a},fd16:function(e,t,r){}});
//# sourceMappingURL=app.52fab43a.js.map