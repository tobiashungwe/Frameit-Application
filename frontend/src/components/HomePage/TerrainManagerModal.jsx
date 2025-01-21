import React, { useEffect, useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  IconButton,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
} from "@mui/material";
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
      <DialogTitle>Manage Terrains</DialogTitle>
      <DialogContent dividers>
        {/* Display existing terrains */}
        <List>
          {terrains.map((terrain) => (
            <ListItem key={terrain.id}>
              {editTerrainId === terrain.id ? (
                <TextField
                  size="small"
                  value={editTerrainName}
                  onChange={(e) => setEditTerrainName(e.target.value)}
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

        {/* Add new terrain */}
        <TextField
          label="New Terrain Name"
          value={newTerrainName}
          onChange={(e) => setNewTerrainName(e.target.value)}
          fullWidth
          margin="dense"
        />
        <Button variant="contained" onClick={handleAddTerrain} sx={{ mt: 1 }}>
          Add Terrain
        </Button>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default TerrainManagerModal;
