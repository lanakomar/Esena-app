import { NavLink } from "react-router-dom";
import "./index.css";

import logo from "../../assets/esena.png";
import ethan from "../../assets/ethan.png";
import lana from "../../assets/lana.jpg";
import vee from "../../assets/vee.png";
import xiaowen from "../../assets/xiaowen.png";

const About = () => {
  return (
    <>
      <div className="developers-container">
        <NavLink to="/">
          <img src={logo} className="about-logo" alt="esena-logo" />
        </NavLink>
        <h1>Thanks for visiting esena.</h1>
        <div className="paragraph-container">
          <p>
            Esena is a project management app inspired by Asana. It is designed
            to make team workflows more organized, structured, and transparent.
          </p>
          <p>Technologies used:</p>
        </div>
        <div className="technologies-container">
          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"
            alt="react-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg"
            alt="redux-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"
            alt="nodejs-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"
            alt="flask-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg"
            alt="sqlalchemy-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
            alt="python-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"
            alt="javascript-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
            alt="github-icon"
          />

          <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"
            alt="docker-icon"
          />
        </div>
        <div className="inner-dev-container">
          <div className="dev-profile">
            <img className="dev-img" src={ethan} alt="Ethan Chen" />
            <h3 className="dev-name">Ethan Chen</h3>
            {/* <p className="dev-area">Los Angeles, California</p> */}
            <div className="logo-container">
              <a href="https://github.com/ethanchen7">
                <i class="fa-brands fa-github-square fa-xl"></i>
              </a>
              <a href="https://www.linkedin.com/in/ethan-chen-3b7070127/">
                <i class="fa-brands fa-linkedin fa-xl"></i>
              </a>
            </div>
          </div>
          <div className="dev-profile">
            <img className="dev-img" src={lana} alt="Lana Komar" />
            <h3 className="dev-name">Lana Komar</h3>
            {/* <p className="dev-area">East Bay, California</p> */}
            <div className="logo-container">
              <a href="https://github.com/lanakomar">
                <i class="fa-brands fa-github-square fa-xl"></i>
              </a>
              <a href="https://www.linkedin.com/in/lana-komar/">
                <i class="fa-brands fa-linkedin fa-xl"></i>
              </a>
            </div>
          </div>
          <div className="dev-profile">
            <img className="dev-img" src={vee} alt="Vee Alianza" />
            <h3 className="dev-name">Vee Alianza</h3>
            {/* <p className="dev-area">Eagle Mountain, Utah</p> */}
            <div className="logo-container">
              <a href="https://github.com/vee-alianza">
                <i class="fa-brands fa-github-square fa-xl"></i>
              </a>
              <a href="https://www.linkedin.com/in/vee-alianza/">
                <i class="fa-brands fa-linkedin fa-xl"></i>
              </a>
            </div>
          </div>
          <div className="dev-profile">
            <img className="dev-img" src={xiaowen} alt="Xiaowen Nie" />
            <h3 className="dev-name">Xiaowen Nie</h3>
            {/* <p className="dev-area">Sunnyvale, California</p> */}
            <div className="logo-container">
              <a href="https://github.com/xwnnie">
                <i class="fa-brands fa-github-square fa-xl"></i>
              </a>
              <a href="https://www.linkedin.com/in/xiaowennie/">
                <i class="fa-brands fa-linkedin fa-xl"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default About;
