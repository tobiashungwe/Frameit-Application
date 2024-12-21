import React, { useState } from 'react';
import { Button, CircularProgress, Typography } from '@mui/material';
import axios from 'axios';

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [sanitizedContent, setSanitizedContent] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) return;
        setLoading(true);
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await axios.post('http://localhost:8000/upload_activity/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setSanitizedContent(response.data.sanitized_content);
        } catch (error) {
            console.error('Error uploading file:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <Button variant="contained" color="primary" onClick={handleUpload} disabled={loading}>
                {loading ? <CircularProgress size={24} /> : 'Upload and Process'}
            </Button>
            {sanitizedContent && (
                <div>
                    <Typography variant="h6">Sanitized Content:</Typography>
                    <Typography>{sanitizedContent}</Typography>
                </div>
            )}
        </div>
    );
};

export default FileUpload;
