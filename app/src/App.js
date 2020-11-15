import logo from './logo.svg';
import './App.css';
import { Button } from '@material-ui/core'
import { jsx } from '@emotion/react'
/** @jsx jsx */ 
/** @jsxRuntime classic */
/** @jsxFrag React.Fragment */
import FileUpload from "./Upload"
import { POST } from './utils'

const onimgupload = (b64) => {

  const payload = {
    input: b64
  }
  POST('http://18.133.254.35:5000', payload)

}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <Button variant='contained'>
          Yo
        </Button>
        <FileUpload onload={onimgupload} />
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

export default App;
