import React from "react";
import {
  BrowserRouter ,
  Switch,
  Route,
  Link,
  Routes
} from "react-router-dom";
import Login from "./Pages/Login";
import Dashboard from "./Pages/Dashboard";

function App() {
return(
  <div>
    <BrowserRouter>
    <Routes>
    <Route exact path='/' element={<Login/>}>
        
      </Route>
      <Route path='/dashboard' element={<Dashboard/>}>
        
      </Route>
    </Routes>
    </BrowserRouter>
  </div>
)
}

export default App;
