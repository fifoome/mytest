import './App.css';
import data from './config.json';
var React = require('react/addons');




var List = React.createClass({
  getInitialState: function() {
    return {data: this.props.data};
  },
  render: function() {
    var listItems = this.state.data.map(function(p) {
      for (var key in p) {
            if (p.hasOwnProperty(key)) {
                return (
                    <td>{p[key]}</td>
                )
            }
        }
    });
    return <ul>{listItems}</ul>
  }
});
var App = React.createClass({
    render: function() {
      return (
        <div>
          <List data={data}/>
        </div>
      );
    }
  });

module.exports = App;

export default App;
