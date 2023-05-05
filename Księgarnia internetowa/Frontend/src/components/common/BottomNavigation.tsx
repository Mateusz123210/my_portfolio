import { useNavigate } from "react-router-dom";

export interface BottomNavigationProps {
    text: string,
    path: string
}

const BottomNavigation = (props: BottomNavigationProps) => {

    const navigate = useNavigate()

    return (
        <button type="button" className="ellipse-back" onClick={() => navigate(props.path)}>
            <div className="left-arrow-line"></div>
            <div className="left-arrow-down"></div>
            <div className="left-arrow-up"></div>
            <div className="left-arrow-down"></div>
            <span className="ellipse-text">{props.text}</span>
        </button>
    )
}

export default BottomNavigation;