import './App.css';
import Sidebar from './Components/Sidebar/Sidebar';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import Home from './Pages/Home';
import Analytics from './Pages/Analytics';
import Dashboard from './Pages/Dashboard';
import Header from './Pages/Header';
function App() {
  const list_symbol=[
    {
      code:'GRAB'
    },
    {
      code:'PFE'
    },
    {
      code:'TSLA'
    },
    {
      code:'NVDA'
    },
    {
      code:'MSFT'
    }
  ]
  return (
    <div className="body">
      <div className='header'><Header></Header></div>
      <div className='nav'><Sidebar></Sidebar></div>     
      <div className='main'>
          <Router>
            <Routes>
              <Route path="/" element={<Home/>}/>
                <Route path="/dashboard" element={<Dashboard/>}/>
                <Route path="/analytics" element={<Analytics list_symbol={list_symbol} range="12mo" region="US" interval="1d" lang="en"/>}/>
              </Routes>
          </Router>
      </div>    
      <div className='footer'></div>          
    </div>
  );
}

export default App;
