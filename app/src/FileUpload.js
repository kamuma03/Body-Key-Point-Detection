import React, {Component} from "react"
import { css } from "@emotion/react"
/** @jsx jsx */ 
/** @jsxRuntime classic */
/** @jsxFrag React.Fragment */
import { jsx } from '@emotion/react'
import { Storage } from "aws-amplify"
import { Button, withTheme } from "@material-ui/core"
import GetAppIcon from '@material-ui/icons/GetApp';

const getStyle = props => {
    let primary = props.theme.palette.primary.main
    let secondary = props.theme.palette.secondary.main
    if (props.color == 'primary') {
        let temp = primary
        primary = secondary
        secondary = temp
    }
    switch (props.variant) {
        case "circular":
            return css`

                .title {
                    width: 100%;
                    justify-content: center;
                    display: flex;
                    font-size: 16px;
                    font-weight: 100; // override font-weight: 900; for .panel>.title elements
                }

                .circle {
                    .display-pic {
                        box-shadow: var(--shadow);
                        overflow: hidden;
                        height: 100%;
                    }

                    .dp-input {
                        cursor: pointer;
                        height: 100%;
                        width: 100%;
                    }

                    .dp-input :hover {
                        opacity: 0.5;
                    }

                    // background-color: ${secondary};
                    border: 10px solid ${secondary};
                    border-radius: 50vw;
                    height: 50vw;
                    width: 50vw;
                    max-height: 200px;
                    max-width: 200px;
                    // width: 200px;
                    margin: 30px auto;
                    overflow: hidden;

                    @media (max-width: 600px) {
                        max-height: 100px;
                        max-width: 100px;
                    }

                    .placeholder {
                        height: 100%;
                        width: 100%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        svg {
                            font-size: 120px;
                            color: ${secondary};
                        }
                    }
                }
            `
        case "row":
        default:
            return css`
                .row {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }

                .preview {
                    img {
                        height: 100px;
                        border-radius: 7px;
                    }
                    width: 100%;
                    display: flex;
                    justify-content: center;
                }
            `
    }
}

class FileUpload extends Component {

    constructor(props) {
        super(props)
        this.state = {
            imgsrc: props.value ? props.value : null,
            preview_img : props.preview ? true : false
        }
    }

    onimgchange = async (e)=>{
        var file = e.target.files[0]
        if(this.props.bucket_filepath && this.props.bucket_url){
            var url = await this.uploadDP(file)
            this.setState({imgsrc: url, filename: file.name})
         }else{
             var reader = new FileReader();
             reader.onload = ()=>{this.setState({imgsrc: e.target.result, filename: file.name})}
             reader.readAsDataURL(file);
         }
    }

    componentDidUpdate = (prevProps, prevState)=>{
        //console.log('updating')
        if(prevState.imgsrc != this.state.imgsrc){
            if (this.props.handleChange) {
                if(this.props.id){
                    this.props.handleChange({id: this.props.id, value: this.state.imgsrc})
                }else{
                    this.props.handleChange(this.state.imgsrc)
                }
            }
        }
    }

    uploadDP = (file) => {
        return new Promise (async (resolve, reject)=>{
            var type
            var url
            var fp
            type = file.type.split('/')[1]
            //this.props.bucket_filepath = enterprise_users/${uuid.v4()}/profile_pic
            //this.props.bucket_url = https://theaicore-data.s3.eu-west-2.amazonaws.com/public/
            fp = `${this.props.bucket_filepath}.${type}`
            //fp = `enterprise_users/${uuid.v4()}/profile_pic.${type}`
            var mimeType 
            if (type == 'png') {
                mimeType = 'image/png'
            }
            else if (type == 'jpg' || type == 'jpeg') {
                mimeType = 'image/jpeg'
            }
            else {
                alert('image type invalid (use .PNG, .JPG or .JPEG images)\nYou used type ' + type)
                return null
            }
                try{
                    var resp = await Storage.put(fp, file, {contentType: mimeType})
                    url =`${this.props.bucket_url}${fp}`
                    resolve(url)
                }catch(e){
                    console.error(e)
                    reject()
                }
        })
    }

    render() {
        switch (this.props.variant) {
            case "circular":
                return <div css={[getStyle(this.props), this.props.style]}>

                    {
                        this.props.show_title == 'top' ?
                        <div className="title">
                            {this.props.title}
                        </div>
                        : null
                    }
                    <div className="circle">
                        <label for="dp-input" className="dp-input">
                            <input accept="image/*" onChange={this.onimgchange} id="dp-input" type="file" style={{display: 'none'}} />
                            {
                                this.state.imgsrc ?
                                <img src={this.state.imgsrc} className="display-pic" alt=""/>
                                : <div className="placeholder">
                                    {this.props.icon ? this.props.icon : <GetAppIcon color={this.props.color ? this.props.color : "primary"} style={{transform: 'rotateZ(180deg)'}}/>}
                                </div>
                            }
                        </label>
                    </div>
                    {
                        this.props.show_title == 'bottom' ?
                        <div className="title">
                            {this.props.title}
                        </div>
                        : null
                    }
                </div>
            case "row":
            default:
                return (
                    <>
                        <div css={[getStyle(this.props), this.props.style]}>
                            <input
                                accept={this.props.type == 'image' ? "image/*": "*"}
                                id="contained-button-file"
                                multiple={this.props.multiple}
                                type="file"
                                style={{display: 'none'}}
                                onChange={this.onimgchange}
                            />
                            <div className="row">
                                {this.props.title ?<p>{this.props.title}</p>:null }
                                <label htmlFor="contained-button-file">
                                    <Button variant="contained" color="primary" component="span" endIcon={this.props.icon ? this.props.icon : <GetAppIcon style={{transform: 'rotateZ(180deg)'}}/>}>
                                        Upload
                                    </Button>
                                </label>
                            </div>
                            {this.props.preview ? 
                                this.state.filename :
                                null
                            }
                            {
                                this.props.type == 'image' && this.state.imgsrc && this.props.preview ?
                                <div className="preview">
                                    <img src={this.state.imgsrc} alt=""/>
                                </div>
                                : null
                            }
                        </div>
                    </>
                )
        }
    }   
}


export default withTheme(FileUpload)