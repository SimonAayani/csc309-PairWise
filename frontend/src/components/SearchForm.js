import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import Select from 'react-select';

import courseList from './data/courseList.js';
import Layout from './Layout';
import { languages, frameworks, concepts } from './data/optionLists.js';

class SearchForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coursecode: "",
      tags: [],
      subhead: "Example: Need a partner for A1!",
      description: "Describe what you're looking for in a partner here.",
    }

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.handleCourseSelection = this.handleCourseSelection.bind(this);
    this.handleTagSelection = this.handleTagSelection.bind(this);
  }

  handleSubmit(e) {
    e.preventDefault();

    const search = {
      coursecode: this.state.coursecode,
      tags: this.state.tags,
      subhead: this.state.subhead,
      description: this.state.description
    }

    console.log("Pretend we just sent an HTTP request with this data:", search);

    this.props.history.push('/results');
  }

  handleChange(e) {
    var change = {};
    change[e.target.name] = e.target.value;
    this.setState(change);
  }

  handleTitleChange(title) {
    var change = {};
    change['subhead'] = title.label;
    this.setState(change);
  };

  handleCourseSelection(course) {
    var change = {};
    change['coursecode'] = course.label;
    this.setState(change);
  };

  handleTagSelection(selection) {
    var tagList = selection.map( (obj) => {
      return obj.label;
    });
    this.setState({tags: tagList});
  }


  render() {
    const courseOptions = courseList.map( (course) => {
      var obj = {
        value: course.id,
        label: course.code,
      };
      return obj;
    })

    return(
        <Layout type="loggedIn">
      <div className="searchForm">
        <h1>New Search</h1>
        <form onSubmit={this.handleSubmit} noValidate >

        <h2>Basic parameters</h2>
          <label>Course code:
            <Select
              isSingle
              name="coursecode"
              onChange={this.handleCourseSelection.bind(this)}
              options={courseOptions}
              placeholder="Start typing your course code!"
            />
          </label>
          <label>A title for your search:
            <input
              className="fakeSelect"
              type="text"
              name="subhead"
              onChange={this.handleChange.bind(this)}
              value={this.state.subhead}
            />
          </label>
          <label>Search description:
          </label>
            <textarea
              className="fakeSelect"
              rows="10"
              name="description"
              onChange={this.handleChange.bind(this)}
              value={this.state.description}
            />

          <h2>Additional filters:</h2>
          <label>Can program in:
            <Select
              isMulti
              name="languages"
              onChange={this.handleTagSelection.bind(this)}
              options={languages}
              openOnClick={false}
              placeholder='Example: JavaScript'
            />
          </label>
          <label>Has experience with:
            <Select
              isMulti
              name="frameworks"
              onChange={this.handleTagSelection.bind(this)}
              options={frameworks}
              openOnClick={false}
              placeholder='Example: Django'
            />
          </label>
          <label>Has expertise in the following fields:
            <Select
              isMulti
              name="concepts"
              onChange={this.handleTagSelection.bind(this)}
              options={concepts}
              openOnClick={false}
              placeholder='Example: Machine Learning'
            />
          </label>
          <label>
            <button type="submit">Submit</button>
          </label>
        </form>
      </div>
  </Layout>
    )
  }
}

export default withRouter(SearchForm);
