import React from "react";
import { Box, Typography, Button } from "@mui/material";
import { useDropzone } from "react-dropzone";

const FileUploader = ({ file, onUploadFile, t }) => {
  const onDrop = (acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      onUploadFile?.(acceptedFiles[0]);
    }
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: {
      "text/plain": [".txt"],
      "application/pdf": [".pdf"],
      "application/msword": [".doc"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"]
    },
  });

  return (
    <>
      <Typography variant="h5" align="center" gutterBottom>
        {t("labels.upload_exercise")}
      </Typography>
      <Box
        {...getRootProps()}
        sx={{
          p: 3,
          border: "2px dashed #aaa",
          borderRadius: 2,
          textAlign: "center",
          cursor: "pointer",
          bgcolor: "#eaeaea",
          "&:hover": { bgcolor: "#f5f5f5" },
        }}
      >
        <input {...getInputProps()} />
        <Typography>
          {file ? file.name : t("placeholders.drag_drop_file")}
        </Typography>
      </Box>
      <Button
        variant="contained"
        color="primary"
        onClick={() => onUploadFile?.(file)} // Safe call
        sx={{ mt: 2 }}
      >
        {t("labels.upload_process")}
      </Button>
    </>
  );
};

export default FileUploader;
