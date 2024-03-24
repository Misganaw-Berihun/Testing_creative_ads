import React, { useState } from "react";

const JsonFileUploader = ({ setJsonFile }) => {
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.readAsText(file, "UTF-8");

      reader.onload = (event) => {
        try {
          const jsonData = JSON.parse(event.target.result);
          setJsonFile(jsonData);
        } catch (error) {
          console.error("Error parsing JSON file:", error);
        }
      };
    }
  };

  return (
    <div>
      <input type="file" accept=".json" onChange={handleFileChange} />
    </div>
  );
};

export default JsonFileUploader;
