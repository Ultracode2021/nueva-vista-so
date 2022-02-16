import SideBar from './components/side-bar';
import Main from './components/main';
import Header from './components/header';

import React from 'react';
import './App.css';

function App() {

  return (
    <div className="App">
         <Header/>
           <div className="general-content">
             <SideBar />
             <Main />
           </div>
    </div>
  );
}

export default App;
