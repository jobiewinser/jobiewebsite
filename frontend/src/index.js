import React from 'react';
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
  for (const project of props.value.projects) {
    projects.push(<li>{project.name}</li>);
  }
  console.log(projects)
  return projects
}
function TopNav() {
  return (
    <Navbar fixed="top" bg="light" expand="lg">
    <Container fluid>
        <Navbar.Brand href="#home">Jobie Winser</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#about_me">About Me</Nav.Link>
            <Nav.Link href="#">Technologies</Nav.Link>
            <Nav.Link href="#projects">Projects</Nav.Link>
            <Nav.Link href="#career">Career and Education</Nav.Link>
            <Nav.Link href="#site">This Site</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
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
              Projects:
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
      fetch("http://portfolio.jobiewinser.co.uk/api/technology/")
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
   
    renderTopNav() {
        return (
            <TopNav/>
        );
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
      if (technology != null){
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
            <div>
                  {this.renderTopNav()}
            </div>
              <Row className="technology-div">
                {this.renderTechnologyDiv()}                
              </Row>
          </div>
        );
    }
}
  
class Game extends React.Component {
    render() {
      return (
        <div className="game">
          <div className="technology-board">
            <TechnologyPage />
          </div>
        </div>
      );
    }
}
  
// ========================================
  
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
  