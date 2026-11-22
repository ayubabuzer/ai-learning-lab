/* Keep the selected language across home and lesson navigation. */
(()=>{'use strict';
 const key='ai-learning-lab-language';
 const params=new URLSearchParams(location.search);
 const fromUrl=params.get('lang');
 let preferred=fromUrl==='ar'||fromUrl==='en'?fromUrl:null;
 try{if(!preferred){const saved=localStorage.getItem(key);if(saved==='ar'||saved==='en')preferred=saved}}catch(_){}
 const button=document.querySelector('#language, #lang, #switchLanguage');
 function current(){return document.documentElement.lang==='ar'?'ar':'en'}
 function persist(){const value=current();try{localStorage.setItem(key,value)}catch(_){};updateLinks(value)}
 function updateLinks(value){for(const a of document.querySelectorAll('a[href]')){
  const raw=a.getAttribute('href');if(!raw||raw.startsWith('#')||/^(?:mailto:|tel:|javascript:)/i.test(raw))continue;
  let url;try{url=new URL(raw,location.href)}catch(_){continue}
  if(url.origin!==location.origin)continue;
  // Only the HTML course routes carry the language, not GitHub or source files.
  if(/\.(?:md|txt|py|zip|png|webp|css|js)$/i.test(url.pathname))continue;
  if(!url.pathname.endsWith('/')&&!url.pathname.endsWith('.html'))continue;
  url.searchParams.set('lang',value);
  a.setAttribute('href',url.pathname+url.search+url.hash);
 }}
 if(button){button.addEventListener('click',()=>{queueMicrotask(persist)})}
 // Page-local initialisation is synchronous and complete before this script runs.
 if(preferred && preferred!==current() && button){button.click()}
 persist();
})();
