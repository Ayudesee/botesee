"""bet_matches created_at

Revision ID: 23843d492270
Revises: cf3ad6b29690
Create Date: 2023-10-22 15:17:41.700790

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "23843d492270"
down_revision = "cf3ad6b29690"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "bet_matches",
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("bet_matches", "created_at")
    # ### end Alembic commands ###
