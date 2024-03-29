import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Routes 
} from "react-router-dom";
import ReactDOM from 'react-dom/client';
import './index.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
    
function renderTechnologyProjects(props) {
  const projects = [];
  for (const [index, project] of props.value.projects.entries()) {
    projects.push(<li key={index}>{project.name}</li>);
  }
  return projects
}
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}
function TechnologyPanel(props) {
  return (
    <Col>
      <Card style={{ width: '18rem' }} className="card">
        <Card.Img variant="top" src={props.value.image} />
        <Card.Body>
          <Card.Title>{props.value.name}</Card.Title>
          <Card.Text>
            Latest Projects:
          </Card.Text>
          <ul>
            {renderTechnologyProjects(props)}
          </ul>
          <Button variant="primary">Go somewhere</Button>
        </Card.Body>
      </Card>
    </Col>
  );
}
  
class TechnologyPage extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        squares: Array(9).fill(null),
        xIsNext: true,
        technologies: Array(1).fill(null),
      };
    }
    componentDidMount() {
      fetch("https://apiportfolio.jobiewinser.co.uk/api/technology/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              technologies: result.results
            });
          },
          (error) => {
            console.log("Error")
          }
        )
    }

    // handleClick(i) {
    //   const squares = this.state.squares.slice();
    //   squares[i] = this.state.xIsNext ? 'X' : 'O';    
    //   this.setState({
    //     squares: squares,
    //     xIsNext: !this.state.xIsNext,
    //   });
    // }

    handleClick(i) {
      console.log(i)
    }
   
    renderSquare(i) {
        return (
            <Square
                value={this.state.squares[i]}
                onClick={() => this.handleClick(i)}
            />
        );
    }
    renderTechnologyPanel(i) {
      let technology = this.state.technologies[i];
      if (technology != null && i != null){
        return (
            <TechnologyPanel
              value={this.state.technologies[i]}
              key={i}
                onClick={() => this.handleClick(i)}
            />
        );
      }
    }
   
    renderTechnologyDiv(i) {
      const technologies = [];
      for (let i = 0; i < this.state.technologies.length; i++) {
        technologies.push(this.renderTechnologyPanel(i));
      }
      return technologies
    }
    
    render() {
        return (
          <div>
              <Row className="technology-div">
                {this.renderTechnologyDiv()}                
              </Row>
          </div>
        );
    }
}
  
export default function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/technologies">Technologies</Link>
            </li>
          </ul>
        </nav>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Routes>
          <Route path='/technologies' element={<TechnologyPage/>} />
        </Routes>
      </div>
    </Router>
  );
}
  
// ========================================
  
// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(<Game />);
  