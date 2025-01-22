import React, { useEffect, useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  IconButton,
  Button,
  TextField,
  Box,
  Grid,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  Typography,
  Divider,
  Paper,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import axios from "axios";

const TerrainManagerModal = ({ open, onClose }) => {
  const [terrains, setTerrains] = useState([]);
  const [newTerrainName, setNewTerrainName] = useState("");
  const [editTerrainId, setEditTerrainId] = useState(null);
  const [editTerrainName, setEditTerrainName] = useState("");

  useEffect(() => {
    if (open) {
      fetchTerrains();
    }
  }, [open]);

  const fetchTerrains = async () => {
    try {
      const response = await axios.get("/api/terrains");
      setTerrains(response.data);
    } catch (err) {
      console.error("Failed to fetch terrains", err);
    }
  };

  const handleAddTerrain = async () => {
    if (!newTerrainName.trim()) return;
    try {
      const response = await axios.post("/api/terrains", null, {
        params: { name: newTerrainName },
      });
      setNewTerrainName("");
      setTerrains([...terrains, response.data]);
    } catch (err) {
      console.error("Failed to create terrain", err);
    }
  };

  const handleEditTerrain = (terrain) => {
    setEditTerrainId(terrain.id);
    setEditTerrainName(terrain.name);
  };

  const handleUpdateTerrain = async () => {
    try {
      const response = await axios.put(`/api/terrains/${editTerrainId}`, null, {
        params: { name: editTerrainName },
      });
      setTerrains(
        terrains.map((t) => (t.id === editTerrainId ? response.data : t))
      );
      setEditTerrainId(null);
      setEditTerrainName("");
    } catch (err) {
      console.error("Failed to update terrain", err);
    }
  };

  const handleDeleteTerrain = async (id) => {
    try {
      await axios.delete(`/api/terrains/${id}`);
      setTerrains(terrains.filter((t) => t.id !== id));
    } catch (err) {
      console.error("Failed to delete terrain", err);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <Typography variant="h6">Manage Terrains</Typography>
        <IconButton onClick={onClose} size="small">
          <CloseIcon />
        </IconButton>
      </DialogTitle>
      <DialogContent dividers>
        {/* Existing Terrains */}
        <Typography variant="subtitle1" sx={{ mb: 1 }}>
          Existing Terrains
        </Typography>
        <Paper variant="outlined" sx={{ maxHeight: 200, overflow: "auto", mb: 3 }}>
          <List>
            {terrains.map((terrain) => (
              <ListItem key={terrain.id} divider>
                {editTerrainId === terrain.id ? (
                  <TextField
                    size="small"
                    value={editTerrainName}
                    onChange={(e) => setEditTerrainName(e.target.value)}
                    fullWidth
                  />
                ) : (
                  <ListItemText primary={terrain.name} />
                )}
                <ListItemSecondaryAction>
                  {editTerrainId === terrain.id ? (
                    <IconButton onClick={handleUpdateTerrain} edge="end">
                      <EditIcon />
                    </IconButton>
                  ) : (
                    <IconButton onClick={() => handleEditTerrain(terrain)} edge="end">
                      <EditIcon />
                    </IconButton>
                  )}
                  <IconButton onClick={() => handleDeleteTerrain(terrain.id)} edge="end">
                    <DeleteIcon />
                  </IconButton>
                </ListItemSecondaryAction>
              </ListItem>
            ))}
          </List>
        </Paper>

        <Divider sx={{ mb: 2 }} />

        {/* Add New Terrain */}
        <Typography variant="subtitle1" sx={{ mb: 1 }}>
          Add New Terrain
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={8}>
            <TextField
              label="Terrain Name"
              value={newTerrainName}
              onChange={(e) => setNewTerrainName(e.target.value)}
              fullWidth
            />
          </Grid>
          <Grid item xs={12} md={4}>
            <Button
              variant="contained"
              fullWidth
              sx={{ height: "100%" }}
              onClick={handleAddTerrain}
            >
              Add
            </Button>
          </Grid>
        </Grid>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="inherit">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default TerrainManagerModal;
