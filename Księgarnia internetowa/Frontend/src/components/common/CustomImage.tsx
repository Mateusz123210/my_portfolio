import React, { useEffect } from "react";

export interface ImageProps {
    img: any,
    width?: number,
    height?: number,
    alt?: string
}

const CustomImage = (props: ImageProps) => {
    const [imgStr, setImgStr] = React.useState<string>('');

    const loadImg = () => {

        if(!props.img)
            return

        setImgStr(props.img);
    }

    useEffect(() => {
        loadImg()
    }, [props])

    return (
        <img 
            alt={props.alt ? props.alt : ""} 
            src={`data:image/jpeg;base64,${imgStr}`} 
            width={props.width ? props.width : 128} 
            height={props.height ? props.height : 204}
        />
    );
}

export default CustomImage;

