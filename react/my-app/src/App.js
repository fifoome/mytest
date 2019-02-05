import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
// import data from './config.json';




class App extends Component {
  render() {
    var f = function() {
      var data = {"data":"fsd"}
      var listItems = []
      for (const [k, v] of Object.entries(data)) {
       listItems += <td>{k} {{v}}</td>
      }


    // console.log(data)
    console.log(listItems)
      return <ul>{listItems}</ul>
    }
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <div>
            {f()}
          </div>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>

        </header>

      </div>
    );
  }
}

export default App;
