(function(){
var input=document.getElementById('q'),list=document.getElementById('results'),count=document.getElementById('count');
function score(doc,terms){var s=0,t=doc.t.toLowerCase(),d=(doc.d+' '+doc.p).toLowerCase(),h=doc.h.join(' ').toLowerCase(),x=doc.x.toLowerCase();
for(var i=0;i<terms.length;i++){var w=terms[i];if(t.indexOf(w)>=0)s+=10;if(h.indexOf(w)>=0)s+=5;if(d.indexOf(w)>=0)s+=3;if(x.indexOf(w)>=0)s+=1;else if(t.indexOf(w)<0&&h.indexOf(w)<0&&d.indexOf(w)<0)return 0;}return s;}
function run(){var q=input.value.trim().toLowerCase();list.innerHTML='';if(!q){count.textContent='';return;}
var terms=q.split(/\s+/),hits=[];for(var i=0;i<AURIC_DOCS.length;i++){var s=score(AURIC_DOCS[i],terms);if(s)hits.push([s,AURIC_DOCS[i]]);}
hits.sort(function(a,b){return b[0]-a[0];});count.textContent=hits.length+' result'+(hits.length===1?'':'s');
hits.slice(0,60).forEach(function(h){var li=document.createElement('li'),a=document.createElement('a');a.href=h[1].u;a.textContent=h[1].t;li.appendChild(a);
var s=document.createElement('small');s.textContent=(h[1].p?h[1].p+' — ':'')+h[1].d;li.appendChild(s);list.appendChild(li);});}
input.addEventListener('input',run);var m=location.search.match(/[?&]q=([^&]*)/);if(m){input.value=decodeURIComponent(m[1].replace(/\+/g,' '));run();}})();
