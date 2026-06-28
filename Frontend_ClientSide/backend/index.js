import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import pg from "pg";
import passport from "passport";
import session from "express-session";
import { Strategy } from "passport-local";
import axios from "axios";

const app = express();
const PORT = 5000;

const db = new pg.Client({
   user:"postgres",
   host:"localhost",
   database:"INDIAPOST",
   password:"@123#",
   port:5432,
})

db.connect();

// Middleware
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

app.use(session({
   secret:"userdetail",
   resave:false,
   saveUninitialized:true,
}))

app.use(passport.initialize());
app.use(passport.session());

app.get('/clicknbook',(req, res)=>{
   if (isAuthenticate()) {
      
   }
   else{
       
   }
});

app.post('/clicknbooksubmit', (req, res) => {
   console.log(req.body);
});

app.post('/usersubmit', (req, res) => {
   console.log(req.body);
});

app.post('/submit', (req, res) => {
   console.log(req.body);
});

passport.use(new Strategy(async function verify(username, password, cb){
      try {
         const result = await db.query("SELECT * FROM userdetail WHERE email = $1",[username,]);
         if(result.rows.length>0){
            const user = result.rows[0];
            const dpassword= user.password;
      
         }
      } catch (error) {
         
      }
}))
// Start the server
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
