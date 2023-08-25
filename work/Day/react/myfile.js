import React, { useState, useEffect } from "react";
import { Col, Row } from "reactstrap";

const SalesPackagesEditor = (props) => {
  const [data, setData] = useState({
    id: "",
    title: "",
    code: "",
    description: "",
    status: "",
    salesRate: "",
    photoFileName: "",
  });

  const [validationErrors, setValidationErrors] = useState({});

  useEffect(() => {
    if (props.data) {
      setData(props.data);
    }
  }, [props.data]);

  const handleInputChange = (event) => {
    setData({
      ...data,
      [event.target.name]: event.target.value,
    });
  };

  const handleSave = () => {
    const newValidationErrors = {};

    if (!data.title) {
      newValidationErrors.title = "Title is required.";
    }
    if (!data.code) {
      newValidationErrors.code = "Code is required.";
    }
    if (!data.description) {
      newValidationErrors.description = "Description is required.";
    }
    if (!data.status) {
      newValidationErrors.status = "Status is required.";
    }
    if (!data.salesRate) {
      newValidationErrors.salesRate = "Sales Rate is required.";
    }
    if (!data.photoFileName) {
      newValidationErrors.photoFileName = "Photo File Name is required.";
    }

    if (Object.keys(newValidationErrors).length === 0) {
      // Save the data and reset the form
      const newId = Date.now();
      const newData = {
        ...data,
        id: newId,
      };

      if (typeof props.onCloseEditor === "function") {
        props.onCloseEditor(newData);
      }

      const existingSalesData = JSON.parse(localStorage.getItem("SalesData")) || [];
      existingSalesData.push(newData);
      localStorage.setItem("SalesData", JSON.stringify(existingSalesData));

      setData({
        id: "",
        title: "",
        code: "",
        description: "",
        status: "",
        salesRate: "",
        photoFileName: "",
      });

      setValidationErrors({});
    } else {
      setValidationErrors(newValidationErrors);
    }
  };

  return (
    <React.Fragment>
    <Row>
      <Col md={6}>
        <Row className="mb-3">
          <Col lg={3}>
            <Label htmlFor="Title">Title</Label>
          </Col>
          <Col lg={9}>
            <Input
              type="text"
              id="Title"
              placeholder="Enter Title"
              value={data.title}
              name="title"
              onChange={handleInputChange}
            />
             {validationErrors.title && <div className="error">{validationErrors.title}</div>}
          </Col>
        </Row>
        <Row className="mb-3">
          <Col lg={3}>
            <Label htmlFor="Code">Code</Label>
          </Col>
          <Col lg={9}>
            <Input
              type="text"
              id="Code"
              placeholder="Enter Code"
              value={data.code}
              name="code"
              onChange={handleInputChange}
            />
             {validationErrors.code && <div className="error">{validationErrors.code}</div>}
          </Col>
        </Row>
        <Row className="mb-3">
          <Col lg={3}>
            <Label htmlFor="Description">Description</Label>
          </Col>
          <Col lg={9}>
            <Input
              type="text"
              id="Description"
              placeholder="Enter Description"
              value={data.description}
              name="description"
              onChange={handleInputChange}
            />
             {validationErrors.description && <div className="error">{validationErrors.description}</div>}
          </Col>
        </Row>
        <Row className="mb-3">
          <Col lg={3}>
            <Label htmlFor="Status">Status</Label>
          </Col>
          <Col lg={9}>
            <Input
              type="number"
              id="Status"
              placeholder="Enter your status"
              value={data.status}
              name="status"
              onChange={handleInputChange}
            />
             {validationErrors.status && <div className="error">{validationErrors.status}</div>}
          </Col>
        </Row>
        <Row className="mb-3">
          <Col lg={3}>
            <Label htmlFor="Salesrate">salesRate</Label>
          </Col>
          <Col lg={9}>
            <Input
              type="number"
              id="Salesrate"
              placeholder="Enter Salesrate"
              value={data.salesRate}
              name="salesRate"
              onChange={handleInputChange}
            />
             {validationErrors.salesRate && <div className="error">{validationErrors.salesRate}</div>}
          </Col>
        </Row>
        <Row className="mb-3">
          <Col lg={3}>
            <Label htmlFor="photoFileName">photoFileName</Label>
          </Col>
          <Col lg={9}>
            <Input
              type="text"
              id="photoFileName"
              placeholder="Enter your photoFileName"
              value={data.photoFileName}
              name="photoFileName"
              onChange={handleInputChange}
            />
             {validationErrors.photoFileName && <div className="error">{validationErrors.photoFileName}</div>}
          </Col>
        </Row>
        <Row>
          <Col>
            <Button onClick={handleSave}>Save</Button>
          </Col>
        </Row>
      </Col>
    </Row>
  </React.Fragment>
  );
};

export default SalesPackagesEditor;
