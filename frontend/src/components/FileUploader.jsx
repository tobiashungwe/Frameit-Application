import React from "react";
import { Box, Typography, Button, Switch, FormControlLabel } from "@mui/material";
import { useDropzone } from "react-dropzone";

const FileUploader = ({ file, onUploadFile, t, useSanitizedContent, setUseSanitizedContent }) => {
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
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
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


            <Box sx={{ mt: 2, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => onUploadFile?.(file)}
                >
                    {t("labels.upload_process")}
                </Button>
                <FormControlLabel
                    control={
                        <Switch
                            checked={useSanitizedContent}
                            onChange={(e) => setUseSanitizedContent(e.target.checked)}
                        />
                    }
                    label={t("labels.remove_theme", "Remove theme for a clearer activity")}
                />
            </Box>
        </>
    );
};

export default FileUploader;
