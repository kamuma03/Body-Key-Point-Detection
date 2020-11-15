import logo from './logo.svg';
import './App.css';
import { Button } from '@material-ui/core'
import { jsx } from '@emotion/react'
/** @jsx jsx */ 
/** @jsxRuntime classic */
/** @jsxFrag React.Fragment */
import FileUpload from "./Upload"
import { POST } from './utils'
import { useState } from 'react';
import placeholder from './image.png';

function App() {

  const [response, setResponse] = useState(placeholder)

  const onimgupload = (b64) => {
    b64 = b64.split(',')[1]
    console.log('b64:', b64)
    const payload = {
      input: b64
    }
    // POST('http://35.178.186.141:5000', payload)
    POST('http://18.133.254.35:5000', payload)
    //POST('http://localhost:5000', payload)
    .then(
      (r) => {
        console.log(r)
        setResponse("data:image/png;base64, " + r.response)
      }
    )
  }

  return (
    <div className="App">
      <div className="Title"> Body Keypoint Detection Using Keypoint R-CNN </div>
      <div className="Description">The WebbApp detects the Body keypoint using Keypoint R-CNN upon uploading an image by the user</div>
      <header className="App-header">
        {
          response ? <img style={{height: '700px', width: '700px', backgroundColor: 'red'}} src={response} /> : null
        }
        <FileUpload onload={onimgupload} />
      </header>
    </div>
  );
}

export default App;
