// Review-only Node.js SMS gateway. NOT deployed. Node 20+.
// Set SMS_OPERATOR_TOKEN, SMS_TO_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER.
// Never commit .env files. Protect endpoint behind TLS and private operator authentication.
// Production requires durable rate limits, audited consent, webhook validation, and security review.
import { createServer } from 'node:http';
import { timingSafeEqual } from 'node:crypto';
const port = Number(process.env.PORT || 8787);
const required = ['SMS_OPERATOR_TOKEN','SMS_TO_NUMBER','TWILIO_ACCOUNT_SID','TWILIO_AUTH_TOKEN','TWILIO_FROM_NUMBER'];
const missing = required.filter(k => !process.env[k]);
if (missing.length) { console.error('Missing required environment variables: '+missing.join(', ')); process.exit(1); }
const eq = (a,b) => { const x=Buffer.from(a||''); const y=Buffer.from(b||''); return x.length===y.length && timingSafeEqual(x,y); };
let lastSend = 0;
const server=createServer(async(req,res)=>{
  const reply=(code,body)=>{res.writeHead(code,{'content-type':'application/json; charset=utf-8','cache-control':'no-store','x-content-type-options':'nosniff'});res.end(JSON.stringify(body));};
  if(req.url!=='/api/sms/confirm'||req.method!=='POST')return reply(404,{error:'not found'});
  if(!eq(req.headers.authorization, 'Bearer '+process.env.SMS_OPERATOR_TOKEN))return reply(401,{error:'unauthorized'});
  if(req.headers['content-type']?.split(';')[0]!=='application/json')return reply(415,{error:'JSON required'});
  let raw='';for await(const chunk of req){raw+=chunk;if(raw.length>2048)return reply(413,{error:'too large'});}
  let input;try{input=JSON.parse(raw);}catch{return reply(400,{error:'invalid JSON'});}
  if(input?.confirm!==true||input?.consent!==true)return reply(400,{error:'explicit confirmation and consent required'});
  if(Date.now()-lastSend<60000)return reply(429,{error:'wait before retrying'});
  lastSend=Date.now();
  const body='InfoFAQs confirmation. Charlie Oscar. Echo. 1 = 1. Reply CONFIRM to acknowledge receipt. Production remains 0 HOLD.';
  const form=new URLSearchParams({To:process.env.SMS_TO_NUMBER,From:process.env.TWILIO_FROM_NUMBER,Body:body});
  const auth=Buffer.from(process.env.TWILIO_ACCOUNT_SID+':'+process.env.TWILIO_AUTH_TOKEN).toString('base64');
  try{
    const response=await fetch('https://api.twilio.com/2010-04-01/Accounts/'+encodeURIComponent(process.env.TWILIO_ACCOUNT_SID)+'/Messages.json',{method:'POST',headers:{authorization:'Basic '+auth,'content-type':'application/x-www-form-urlencoded'},body:form,signal:AbortSignal.timeout(12000)});
    const result=await response.json();
    if(!response.ok)return reply(502,{status:'provider_error',code:result.code||null});
    return reply(202,{status:'accepted_not_delivered',provider_message_id:result.sid||null});
  }catch{return reply(502,{status:'provider_unreachable'});}
});
server.listen(port,'127.0.0.1',()=>console.log('Review-only SMS gateway listening on localhost:'+port));
