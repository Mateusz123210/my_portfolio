import React from "react";
import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import Forbidden from "../../pages/errors/Forbidden";
import { RootState } from "../../redux/store";

type ProtectedRouteProps = {
    children: React.ReactNode,
    isNotLogged: boolean,
    isClient: boolean,
    isEmployee: boolean
};

const ProtectedRoute = (props: ProtectedRouteProps) => {

    const userDetails = useSelector((state: RootState) => state.user);

    if(props.isNotLogged){
        return <React.Fragment>{props.children}</React.Fragment>
    }

    if(props.isClient){
        return userDetails.clientId ? <React.Fragment>{props.children}</React.Fragment> : <Forbidden/>
    }

    if(props.isEmployee){
        return (userDetails.isLogged && !userDetails.clientId) ? <React.Fragment>{props.children}</React.Fragment> : <Forbidden/>
    }

    return <div></div>
}

export default ProtectedRoute;