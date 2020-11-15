import React, {Component, useState } from "react"
import { css } from "@emotion/react"
/** @jsx jsx */ 
/** @jsxRuntime classic */
/** @jsxFrag React.Fragment */
import { jsx } from '@emotion/react'
import { Storage } from "aws-amplify"
import { Button, withTheme } from "@material-ui/core"
import GetAppIcon from '@material-ui/icons/GetApp';

const getStyle = props => null

const Upload = props => {

    const [imgsrc, setImgsrc] = useState()
    const [filename, setFilename] = useState()
    console.log(imgsrc)

    const onimgchange = async (e)=>{
        console.log('img changing')
        var file = e.target.files[0]
        console.log(e.target.result)
        // if (props.bucket_filepath && props.bucket_url) {
        //     var url = await this.uploadDP(file)
        //     setImgsrc(url)
        //     // ,filename: file.name})
        //  }
        //  else {
             var reader = new FileReader();
             reader.onload = ()=>{                 
                 setImgsrc(e.target.result)
                 console.log(reader.result)
                 props.onload(reader.result)
             }
                //  filename: file.name
             reader.readAsDataURL(file);
        //  }
    }

    return <div css={[getStyle(props), props.style]}>
        <input
            accept={props.type == 'image' ? "image/*": "*"}
            id="contained-button-file"
            multiple={props.multiple}
            type="file"
            style={{display: 'none'}}
            onChange={onimgchange}
        />
        <div className="row">
            {props.title ?<p>{props.title}</p>:null }
            <label htmlFor="contained-button-file">
                <Button variant="contained" color="primary" component="span" endIcon={props.icon ? props.icon : <GetAppIcon style={{transform: 'rotateZ(180deg)'}}/>}>
                    Upload
                </Button>
            </label>
        </div>
        {props.preview ? 
            filename :
            null
        }
        {
            props.type == 'image' && imgsrc && props.preview ?
            <div className="preview">
                <img src={imgsrc} alt=""/>
            </div>
            : null
        }
    </div>
}

export default Upload